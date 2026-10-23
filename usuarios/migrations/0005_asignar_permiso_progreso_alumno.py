from django.db import migrations


def asignar_permiso_progreso_alumno(apps, schema_editor):
    Permiso = apps.get_model("usuarios", "Permiso")
    Perfil = apps.get_model("usuarios", "Perfil")
    PerfilTienePermiso = apps.get_model("usuarios", "PerfilTienePermiso")
    database = schema_editor.connection.alias

    permiso, _ = Permiso.objects.using(database).update_or_create(
        codename="view_progreso_asistencia",
        defaults={
            "tipo": "asistencia_clase",
            "nombre": "Ver progreso de asistencia a clases",
        },
    )
    perfil_alumno = Perfil.objects.using(database).filter(
        nombre__iexact="alumno"
    ).first()

    if perfil_alumno is None:
        raise RuntimeError(
            "No se encontró el perfil 'alumno' para asignarle "
            "asistencia_clase.view_progreso_asistencia."
        )

    PerfilTienePermiso.objects.using(database).get_or_create(
        perfil_id=perfil_alumno.pk,
        permiso_id=permiso.pk,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0004_asignar_permiso_home_alumno"),
    ]

    operations = [
        migrations.RunPython(
            asignar_permiso_progreso_alumno,
            migrations.RunPython.noop,
        ),
    ]
