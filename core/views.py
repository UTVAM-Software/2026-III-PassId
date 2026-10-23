
from django.views.generic import TemplateView
from core.mixins import PassIdPermissionMixin

from core.utils import generar_qr


class HomeView(PassIdPermissionMixin, TemplateView):
    template_name = "core/home.html"
    required_permission = "core.view_home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user

        identificador = (
            getattr(usuario, "matricula", None)
            or usuario.username
        )

        context["qr_base64"] = generar_qr(identificador)

        return context
