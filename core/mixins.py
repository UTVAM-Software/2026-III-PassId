from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect

class PassIdPermissionMixin(LoginRequiredMixin):
    """
    Mixin para CBV que valida:
    1. Usuario autenticado (LoginRequiredMixin).
    2. Validación de permiso atómico o modular (required_permission: 'tipo.codename').
       Los superusuarios tienen acceso total.
    """
    required_permission = None

    def dispatch(self, request, *args, **kwargs):
        if not self.required_permission:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} must define required_permission as 'tipo.codename'."
            )

        tipo, separator, codename = self.required_permission.partition(".")
        if not separator or not tipo or not codename or "." in codename:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__}.required_permission must use the 'tipo.codename' format."
            )

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not (request.user.is_superuser or request.user.has_perm(self.required_permission)):
            messages.error(
                request,
                f"Acceso denegado: Se requiere el permiso '{self.required_permission}' para realizar esta acción."
            )
            referer = request.META.get("HTTP_REFERER")
            if referer and referer != request.build_absolute_uri():
                return redirect(referer)
            raise PermissionDenied(f"No tienes el permiso requerido: {self.required_permission}")

        return super().dispatch(request, *args, **kwargs)
