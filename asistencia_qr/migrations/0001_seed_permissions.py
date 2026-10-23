from django.db import migrations


PERMISSIONS = (
    ("ver_mi_qr", "Consultar el QR propio de asistencia"),
    ("escanear_asistencia", "Registrar asistencia mediante QR"),
    ("ver_asistencias", "Consultar asistencias de clase"),
)


def create_permissions(apps, schema_editor):
    Permiso = apps.get_model("usuarios", "Permiso")
    for codename, nombre in PERMISSIONS:
        Permiso.objects.using(schema_editor.connection.alias).get_or_create(
            tipo="asistencia_qr",
            codename=codename,
            defaults={"nombre": nombre},
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("usuarios", "0002_alter_usuario_superusuario_and_more"),
    ]

    operations = [
        migrations.RunPython(create_permissions, migrations.RunPython.noop),
    ]
