import base64

from django.core import signing
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from academico.models import AsistenciaClase, Inscripcion
from core.mixins import PassIdPermissionMixin
from core.utils import generar_qr
from usuarios.models import Usuario

from .forms import EscaneoAsistenciaForm


QR_SIGNING_SALT = "asistencia_qr.matricula"
QR_TOKEN_MAX_AGE_SECONDS = 300


class MiQrView(PassIdPermissionMixin, TemplateView):
    template_name = "asistencia_qr/mi_qr.html"
    required_permission = "asistencia_qr.ver_mi_qr"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["matricula"] = self.request.user.matricula
        return context


@method_decorator(never_cache, name="dispatch")
class QrImagenView(PassIdPermissionMixin, View):
    required_permission = "asistencia_qr.ver_mi_qr"

    def get(self, request, *args, **kwargs):
        matricula = request.user.matricula
        if not matricula:
            return HttpResponse(
                "Tu cuenta no tiene una matrícula registrada.",
                status=400,
                content_type="text/plain; charset=utf-8",
            )

        token = signing.dumps(
            {"matricula": matricula},
            salt=QR_SIGNING_SALT,
            compress=True,
        )
        response = HttpResponse(
            base64.b64decode(generar_qr(token)),
            content_type="image/png",
        )
        response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return response


class EscanearAsistenciaView(PassIdPermissionMixin, TemplateView):
    template_name = "asistencia_qr/lector.html"
    required_permission = "asistencia_qr.escanear_asistencia"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EscaneoAsistenciaForm(user=self.request.user)
        return context


class RegistrarAsistenciaQrView(PassIdPermissionMixin, View):
    required_permission = "asistencia_qr.escanear_asistencia"

    def post(self, request, *args, **kwargs):
        form = EscaneoAsistenciaForm(request.POST, user=request.user)
        if not form.is_valid():
            return JsonResponse(
                {"ok": False, "message": "Selecciona una clase y escanea un QR válido."},
                status=400,
            )

        token = form.cleaned_data["token"]
        if token:
            try:
                payload = signing.loads(
                    token,
                    salt=QR_SIGNING_SALT,
                    max_age=QR_TOKEN_MAX_AGE_SECONDS,
                )
            except signing.SignatureExpired:
                return JsonResponse(
                    {"ok": False, "message": "El QR venció. Pide al estudiante que actualice su código."},
                    status=400,
                )
            except signing.BadSignature:
                return JsonResponse(
                    {"ok": False, "message": "El QR no es válido o fue alterado."},
                    status=400,
                )

            matricula = payload.get("matricula") if isinstance(payload, dict) else None
            if not isinstance(matricula, str) or not matricula:
                return JsonResponse(
                    {"ok": False, "message": "El QR no contiene una matrícula válida."},
                    status=400,
                )
            metodo = "qr"
        else:
            matricula = form.cleaned_data["matricula"]
            metodo = "manual"

        usuarios = list(
            Usuario.objects.filter(matricula=matricula, activo=True).order_by("pk")[:2]
        )
        if len(usuarios) != 1:
            return JsonResponse(
                {"ok": False, "message": "No se encontró una cuenta activa única para esa matrícula."},
                status=404,
            )
        estudiante = usuarios[0]
        horario = form.cleaned_data["horario"]
        inscrito = Inscripcion.objects.filter(
            usuario=estudiante,
            materia=horario.materia,
            grupo=horario.grupo,
            periodo=horario.periodo,
            activa=True,
        ).exists()
        if not inscrito:
            return JsonResponse(
                {
                    "ok": False,
                    "message": "El estudiante no tiene inscripción activa en esta clase, grupo y periodo.",
                },
                status=403,
            )

        ahora = timezone.localtime()
        asistencia, creada = AsistenciaClase.objects.get_or_create(
            horario=horario,
            usuario=estudiante,
            fecha=ahora.date(),
            defaults={
                "hora": ahora.time().replace(microsecond=0),
                "estado": "presente",
                "metodo": metodo,
            },
        )
        if not creada:
            return JsonResponse(
                {
                    "ok": False,
                    "duplicate": True,
                    "message": f"{estudiante} ya tiene asistencia registrada para esta clase hoy.",
                },
                status=409,
            )

        return JsonResponse(
            {
                "ok": True,
                "message": f"Asistencia registrada para {estudiante} ({matricula}).",
                "matricula": matricula,
                "hora": asistencia.hora.strftime("%H:%M:%S"),
            }
        )


class AsistenciaClaseListView(PassIdPermissionMixin, ListView):
    model = AsistenciaClase
    template_name = "asistencia_qr/asistencia_list.html"
    context_object_name = "asistencias"
    paginate_by = 25
    required_permission = "asistencia_qr.ver_asistencias"

    def get_queryset(self):
        asistencias = AsistenciaClase.objects.select_related(
            "usuario", "horario", "horario__materia"
        )
        if not self.request.user.is_superuser:
            asistencias = asistencias.filter(horario__profesor=self.request.user)
        return asistencias.order_by("-fecha", "-hora")
