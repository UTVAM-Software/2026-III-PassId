from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db import transaction
from django.views.generic import CreateView
from django.utils.text import slugify
from usuarios.models import Perfil
from .forms import LoginForm, RegistroUsuarioForm

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "autenticacion/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"¡Bienvenido de nuevo, {user.nombre or user.username}!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")

class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = "autenticacion/registro.html"
    success_url = reverse_lazy("autenticacion:login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        perfiles_por_nombre = {
            slugify(perfil.nombre): perfil
            for perfil in Perfil.objects.all()
        }
        perfiles_disponibles = [
            perfiles_por_nombre.get("basico"),
            perfiles_por_nombre.get("alumno"),
        ]
        perfiles_asignables = [
            perfil for perfil in perfiles_disponibles if perfil is not None
        ]
        if not perfiles_asignables:
            form.add_error(
                None,
                "No es posible crear una cuenta porque no está disponible el perfil "
                "Básico ni el perfil Alumno. Contacta al administrador.",
            )
            return self.form_invalid(form)

        response = super().form_valid(form)
        self.object.perfiles.add(*perfiles_asignables)
        messages.success(self.request, "Tu cuenta se creó correctamente. Ya puedes iniciar sesión.")
        return response

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("autenticacion:login")
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, "Has cerrado sesión correctamente.")
        return response
