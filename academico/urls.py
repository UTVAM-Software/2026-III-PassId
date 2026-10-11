from django.urls import path
from .views import (
    CarreraListView, CarreraCreateView, CarreraUpdateView, CarreraDeleteView,
    AulaListView, AulaCreateView, AulaUpdateView, AulaDeleteView,
    MateriaListView, MateriaCreateView, MateriaUpdateView, MateriaDeleteView,
    HorarioListView, HorarioCreateView, HorarioUpdateView, HorarioDeleteView,
    InscripcionListView, InscripcionCreateView, InscripcionUpdateView, InscripcionDeleteView,
)

app_name = "academico"

urlpatterns = [
    # Carreras
    path("carreras/", CarreraListView.as_view(), name="carrera_list"),
    path("carreras/crear/", CarreraCreateView.as_view(), name="carrera_create"),
    path("carreras/<int:pk>/editar/", CarreraUpdateView.as_view(), name="carrera_update"),
    path("carreras/<int:pk>/eliminar/", CarreraDeleteView.as_view(), name="carrera_delete"),

    # Aulas
    path("aulas/", AulaListView.as_view(), name="aula_list"),
    path("aulas/crear/", AulaCreateView.as_view(), name="aula_create"),
    path("aulas/<int:pk>/editar/", AulaUpdateView.as_view(), name="aula_update"),
    path("aulas/<int:pk>/eliminar/", AulaDeleteView.as_view(), name="aula_delete"),

    # Materias
    path("materias/", MateriaListView.as_view(), name="materia_list"),
    path("materias/crear/", MateriaCreateView.as_view(), name="materia_create"),
    path("materias/<int:pk>/editar/", MateriaUpdateView.as_view(), name="materia_update"),
    path("materias/<int:pk>/eliminar/", MateriaDeleteView.as_view(), name="materia_delete"),

    # Horarios
    path("horarios/", HorarioListView.as_view(), name="horario_list"),
    path("horarios/crear/", HorarioCreateView.as_view(), name="horario_create"),
    path("horarios/<int:pk>/editar/", HorarioUpdateView.as_view(), name="horario_update"),
    path("horarios/<int:pk>/eliminar/", HorarioDeleteView.as_view(), name="horario_delete"),

    # Inscripciones
    path("inscripciones/", InscripcionListView.as_view(), name="inscripcion_list"),
    path("inscripciones/crear/", InscripcionCreateView.as_view(), name="inscripcion_create"),
    path("inscripciones/<int:pk>/editar/", InscripcionUpdateView.as_view(), name="inscripcion_update"),
    path("inscripciones/<int:pk>/eliminar/", InscripcionDeleteView.as_view(), name="inscripcion_delete"),
]
