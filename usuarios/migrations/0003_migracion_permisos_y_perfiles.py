from django.db import migrations

PERMISOS = [
    {"id": 1, "tipo": "permiso", "codename": "add_permiso", "nombre": "Agregar permiso"},
    {"id": 2, "tipo": "permiso", "codename": "change_permiso", "nombre": "Cambiar permiso"},
    {"id": 3, "tipo": "permiso", "codename": "delete_permiso", "nombre": "Eliminar permiso"},
    {"id": 4, "tipo": "permiso", "codename": "view_permiso", "nombre": "Ver permiso"},
    {"id": 5, "tipo": "permiso", "codename": "list_permiso", "nombre": "Listar permisos"},
    {"id": 6, "tipo": "perfil", "codename": "add_perfil", "nombre": "Agregar perfil"},
    {"id": 7, "tipo": "perfil", "codename": "change_perfil", "nombre": "Cambiar perfil"},
    {"id": 8, "tipo": "perfil", "codename": "delete_perfil", "nombre": "Eliminar perfil"},
    {"id": 9, "tipo": "perfil", "codename": "view_perfil", "nombre": "Ver perfil"},
    {"id": 10, "tipo": "perfil", "codename": "list_perfil", "nombre": "Listar perfiles"},
    {"id": 11, "tipo": "usuario", "codename": "add_usuario", "nombre": "Agregar usuario"},
    {"id": 12, "tipo": "usuario", "codename": "change_usuario", "nombre": "Cambiar usuario"},
    {"id": 13, "tipo": "usuario", "codename": "delete_usuario", "nombre": "Eliminar usuario"},
    {"id": 14, "tipo": "usuario", "codename": "view_usuario", "nombre": "Ver usuario"},
    {"id": 15, "tipo": "usuario", "codename": "list_usuario", "nombre": "Listar usuarios"},
    {"id": 16, "tipo": "evento", "codename": "add_evento", "nombre": "Agregar evento"},
    {"id": 17, "tipo": "evento", "codename": "change_evento", "nombre": "Cambiar evento"},
    {"id": 18, "tipo": "evento", "codename": "delete_evento", "nombre": "Eliminar evento"},
    {"id": 19, "tipo": "evento", "codename": "view_evento", "nombre": "Ver evento"},
    {"id": 20, "tipo": "evento", "codename": "list_evento", "nombre": "Listar eventos"},
    {"id": 21, "tipo": "migracion", "codename": "view_migracion", "nombre": "Ver menú de migraciones"},
    {"id": 22, "tipo": "migracion", "codename": "run_migracion", "nombre": "Ejecutar sincronización de migraciones"},
    {"id": 25, "tipo": "usuario", "codename": "add_usuario_masivo", "nombre": "Agregar usuarios de forma masiva"},
    {"id": 26, "tipo": "otro", "codename": "registrar_en_evento_rapido", "nombre": "Registrar usuarios rápidamente en eventos"},
    {"id": 27, "tipo": "otro", "codename": "registrar_en_evento", "nombre": "Registrar usuarios eventos (administrar registros a eventos)"},
    {"id": 28, "tipo": "evento", "codename": "add_evento_masivo", "nombre": "Agregar eventos de forma masiva"},
    {"id": 29, "tipo": "asistencia", "codename": "view_asistencia", "nombre": "Ver módulo de asistencia"},
    {"id": 30, "tipo": "asistencia", "codename": "add_asistencia", "nombre": "Registrar nueva asistencia"},
    {"id": 31, "tipo": "asistencia", "codename": "delete_asistencia", "nombre": "Eliminar registros de asistencia"},
    {"id": 32, "tipo": "asistencia", "codename": "asistencia.*", "nombre": "Control total de asistencia"},
    {"id": 33, "tipo": "usuario", "codename": "restaturar_contraseña_otros", "nombre": "Restaurar la contraseña de otros usuarios"},
    {"id": 34, "tipo": "otro", "codename": "restaturar_contraseña", "nombre": "Restaurar mi contraseña"},
    {"id": 35, "tipo": "otro", "codename": "update_perfil", "nombre": "Actualizar mi perfil"},
    {"id": 36, "tipo": "otro", "codename": "autorregistrarse", "nombre": "Registrarse a sí mismo en eventos (Autorregistro)"},
    {"id": 37, "tipo": "reporte", "codename": "usuario", "nombre": "Reporte de Usuarios"},
    {"id": 38, "tipo": "reporte", "codename": "evento", "nombre": "Reporte de Eventos"},
    {"id": 39, "tipo": "reporte", "codename": "evento-usuario", "nombre": "Reporte Evento - Usuario"},
    {"id": 40, "tipo": "carrera", "codename": "add_carrera", "nombre": "Agregar carrera"},
    {"id": 41, "tipo": "carrera", "codename": "change_carrera", "nombre": "Cambiar carrera"},
    {"id": 42, "tipo": "carrera", "codename": "delete_carrera", "nombre": "Eliminar carrera"},
    {"id": 43, "tipo": "carrera", "codename": "view_carrera", "nombre": "Ver carrera"},
    {"id": 44, "tipo": "aula", "codename": "add_aula", "nombre": "Agregar aula"},
    {"id": 45, "tipo": "aula", "codename": "change_aula", "nombre": "Cambiar aula"},
    {"id": 46, "tipo": "aula", "codename": "delete_aula", "nombre": "Eliminar aula"},
    {"id": 47, "tipo": "aula", "codename": "view_aula", "nombre": "Ver aula"},
    {"id": 48, "tipo": "materia", "codename": "add_materia", "nombre": "Agregar materia"},
    {"id": 49, "tipo": "materia", "codename": "change_materia", "nombre": "Cambiar materia"},
    {"id": 50, "tipo": "materia", "codename": "delete_materia", "nombre": "Eliminar materia"},
    {"id": 51, "tipo": "materia", "codename": "view_materia", "nombre": "Ver materia"},
    {"id": 52, "tipo": "horario", "codename": "add_horario", "nombre": "Agregar horario"},
    {"id": 53, "tipo": "horario", "codename": "change_horario", "nombre": "Cambiar horario"},
    {"id": 54, "tipo": "horario", "codename": "delete_horario", "nombre": "Eliminar horario"},
    {"id": 55, "tipo": "horario", "codename": "view_horario", "nombre": "Ver horario"},
    {"id": 56, "tipo": "horario", "codename": "manage_disponibilidad", "nombre": "Gestionar disponibilidad de horarios"},
    {"id": 71, "tipo": "horario", "codename": "view_carga_academica", "nombre": "Ver mi carga académica"},
    {"id": 74, "tipo": "asistencia_clase", "codename": "pasar_lista", "nombre": "Pasar lista de asistencia (QR)"},
    {"id": 75, "tipo": "asistencia_clase", "codename": "ver_mi_asistencia", "nombre": "Ver mi propia asistencia"},
    {"id": 76, "tipo": "asistencia_clase", "codename": "ver_historial", "nombre": "Ver historial de asistencia de mis grupos"},
    {"id": 77, "tipo": "inscripcion", "codename": "add_inscripcion", "nombre": "Agregar inscripcion"},
    {"id": 78, "tipo": "inscripcion", "codename": "change_inscripcion", "nombre": "Cambiar inscripcion"},
    {"id": 79, "tipo": "inscripcion", "codename": "delete_inscripcion", "nombre": "Eliminar inscripcion"},
    {"id": 80, "tipo": "inscripcion", "codename": "view_inscripcion", "nombre": "Ver inscripcion"},
]

PERFILES = [
    {"id": 1, "nombre": "basico"},
    {"id": 2, "nombre": "alumno"},
    {"id": 3, "nombre": "admin"},
    {"id": 4, "nombre": "profesor"},
    {"id": 5, "nombre": "qa"},
    {"id": 6, "nombre": "dev"},
]

PERFIL_TIENE_PERMISO = [
    
    {"perfil_id": 2, "permiso_id": 75},
    {"perfil_id": 3, "permiso_id": 40},
    {"perfil_id": 3, "permiso_id": 41},
    {"perfil_id": 3, "permiso_id": 42},
    {"perfil_id": 3, "permiso_id": 43},
    {"perfil_id": 3, "permiso_id": 44},
    {"perfil_id": 3, "permiso_id": 45},
    {"perfil_id": 3, "permiso_id": 46},
    {"perfil_id": 3, "permiso_id": 47},
    {"perfil_id": 3, "permiso_id": 48},
    {"perfil_id": 3, "permiso_id": 49},
    {"perfil_id": 3, "permiso_id": 50},
    {"perfil_id": 3, "permiso_id": 51},
    {"perfil_id": 3, "permiso_id": 52},
    {"perfil_id": 3, "permiso_id": 53},
    {"perfil_id": 3, "permiso_id": 54},
    {"perfil_id": 3, "permiso_id": 55},
    {"perfil_id": 3, "permiso_id": 56},
    {"perfil_id": 3, "permiso_id": 71},
    {"perfil_id": 3, "permiso_id": 74},
    {"perfil_id": 3, "permiso_id": 75},
    {"perfil_id": 3, "permiso_id": 76},
    {"perfil_id": 3, "permiso_id": 77},
    {"perfil_id": 3, "permiso_id": 78},
    {"perfil_id": 3, "permiso_id": 79},
    {"perfil_id": 3, "permiso_id": 80},
    {"perfil_id": 4, "permiso_id": 56},
    {"perfil_id": 4, "permiso_id": 71},
    {"perfil_id": 4, "permiso_id": 74},
    {"perfil_id": 4, "permiso_id": 76},
]


def aplicar_migracion(apps, schema_editor):
    Permiso = apps.get_model("usuarios", "Permiso")
    Perfil = apps.get_model("usuarios", "Perfil")
    PerfilTienePermiso = apps.get_model("usuarios", "PerfilTienePermiso")

    PerfilTienePermiso.objects.filter(perfil_id=1, permiso_id=1).delete()
    Permiso.objects.filter(codename="View_Modulon").delete()
    Perfil.objects.filter(nombre="Permite ver el Modulon").delete()

    for p in PERMISOS:
        Permiso.objects.update_or_create(
            id=p["id"],
            defaults={
                "tipo": p["tipo"],
                "codename": p["codename"],
                "nombre": p["nombre"],
            }
        )

    for pf in PERFILES:
        Perfil.objects.update_or_create(
            id=pf["id"],
            defaults={
                "nombre": pf["nombre"],
            }
        )

    for ptp in PERFIL_TIENE_PERMISO:
        PerfilTienePermiso.objects.get_or_create(
            perfil_id=ptp["perfil_id"],
            permiso_id=ptp["permiso_id"],
        )


def revertir_migracion(apps, schema_editor):
    Permiso = apps.get_model("usuarios", "Permiso")
    Perfil = apps.get_model("usuarios", "Perfil")
    PerfilTienePermiso = apps.get_model("usuarios", "PerfilTienePermiso")

    PerfilTienePermiso.objects.all().delete()
    Perfil.objects.filter(id__in=[pf["id"] for pf in PERFILES]).delete()
    Permiso.objects.filter(id__in=[p["id"] for p in PERMISOS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_alter_usuario_superusuario_and_more"),
    ]

    operations = [
        migrations.RunPython(aplicar_migracion, revertir_migracion),
    ]
