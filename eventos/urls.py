from django.urls import path
from .views import (
    EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView,
    RegistroListView, RegistroCreateView, RegistroUpdateView, RegistroDeleteView,
    AsistenciaListView, AsistenciaCreateView, AsistenciaDeleteView,
)

app_name = "eventos"

urlpatterns = [
    # Eventos
    path("", EventoListView.as_view(), name="evento_list"),
    path("crear/", EventoCreateView.as_view(), name="evento_create"),
    path("<int:pk>/editar/", EventoUpdateView.as_view(), name="evento_update"),
    path("<int:pk>/eliminar/", EventoDeleteView.as_view(), name="evento_delete"),

    # Pre-registros
    path("registros/", RegistroListView.as_view(), name="registro_list"),
    path("registros/crear/", RegistroCreateView.as_view(), name="registro_create"),
    path("registros/<int:pk>/editar/", RegistroUpdateView.as_view(), name="registro_update"),
    path("registros/<int:pk>/eliminar/", RegistroDeleteView.as_view(), name="registro_delete"),

    # Asistencias
    path("asistencias/", AsistenciaListView.as_view(), name="asistencia_list"),
    path("asistencias/crear/", AsistenciaCreateView.as_view(), name="asistencia_create"),
    path("asistencias/<int:pk>/eliminar/", AsistenciaDeleteView.as_view(), name="asistencia_delete"),
]
