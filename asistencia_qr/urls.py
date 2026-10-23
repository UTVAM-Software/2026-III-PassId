from django.urls import path

from .views import (
    AsistenciaClaseListView,
    EscanearAsistenciaView,
    MiQrView,
    QrImagenView,
    RegistrarAsistenciaQrView,
)

app_name = "asistencia_qr"

urlpatterns = [
    path("mi-qr/", MiQrView.as_view(), name="mi_qr"),
    path("mi-qr/imagen.png", QrImagenView.as_view(), name="qr_imagen"),
    path("lector/", EscanearAsistenciaView.as_view(), name="lector"),
    path("registrar/", RegistrarAsistenciaQrView.as_view(), name="registrar"),
    path("asistencias/", AsistenciaClaseListView.as_view(), name="asistencia_list"),
]
