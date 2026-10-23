
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class PassIdPermissionMixin(LoginRequiredMixin):
    """
    Control de acceso para vistas basadas en clases.

    - Requiere autenticación.
    - Valida permisos con formato 'tipo.codename'.
    - Permite acceso total a superusuarios.
    - No revela información interna de permisos al usuario.
    """

    required_permission = None

    def dispatch(self, request, *args, **kwargs):
        if not self.required_permission:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} must define required_permission."
            )

        tipo, separator, codename = self.required_permission.partition(".")

        if not separator or not tipo or not codename or "." in codename:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__}.required_permission "
                "must use the 'tipo.codename' format."
            )

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if (
            not request.user.is_superuser
            and not request.user.has_perm(self.required_permission)
        ):
            messages.error(request, "Acceso denegado.")
            return redirect(reverse("home"))

        return super().dispatch(request, *args, **kwargs)
