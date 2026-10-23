from django.db import migrations


def asignar_permiso_home_alumno(apps, schema_editor):
    Permiso = apps.get_model("usuarios", "Permiso")
    Perfil = apps.get_model("usuarios", "Perfil")
    PerfilTienePermiso = apps.get_model("usuarios", "PerfilTienePermiso")
    database = schema_editor.connection.alias

    permiso, _ = Permiso.objects.using(database).update_or_create(
        codename="view_home",
        defaults={
            "tipo": "core",
            "nombre": "Ver página principal",
        },
    )
    perfil_alumno = Perfil.objects.using(database).filter(
        nombre__iexact="alumno"
    ).first()

    if perfil_alumno is None:
        raise RuntimeError(
            "No se encontró el perfil 'alumno' para asignarle core.view_home."
        )

    PerfilTienePermiso.objects.using(database).get_or_create(
        perfil_id=perfil_alumno.pk,
        permiso_id=permiso.pk,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0003_migracion_permisos_y_perfiles"),
    ]

    operations = [
        migrations.RunPython(
            asignar_permiso_home_alumno,
            migrations.RunPython.noop,
        ),
    ]
