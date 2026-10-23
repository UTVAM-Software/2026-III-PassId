from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegistroUsuarioView

app_name = "autenticacion"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", RegistroUsuarioView.as_view(), name="registro"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
