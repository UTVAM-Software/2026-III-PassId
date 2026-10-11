from django import forms
from .models import Evento, Registro, Asistencia

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            "nombre", "fecha_hora", "lugar",
            "requiere_registro", "permitir_autorregistro",
            "responsable_interno", "responsable_externo",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del evento"}),
            "fecha_hora": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "lugar": forms.TextInput(attrs={"class": "form-control", "placeholder": "Auditorio, Aula Magna, etc."}),
            "requiere_registro": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "permitir_autorregistro": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "responsable_interno": forms.TextInput(attrs={"class": "form-control", "placeholder": "Responsable interno"}),
            "responsable_externo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Responsable externo o ponente"}),
        }


class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ["evento", "usuario", "equipo"]
        widgets = {
            "evento": forms.Select(attrs={"class": "form-select"}),
            "usuario": forms.Select(attrs={"class": "form-select"}),
            "equipo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de equipo (opcional)"}),
        }


class AsistenciaEventoForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ["evento", "usuario"]
        widgets = {
            "evento": forms.Select(attrs={"class": "form-select"}),
            "usuario": forms.Select(attrs={"class": "form-select"}),
        }
