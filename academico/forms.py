from django import forms
from .models import Carrera, Aula, Materia, Horario, Inscripcion

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ["clave", "nombre", "activa"]
        widgets = {
            "clave": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. ITI, MECA"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre completo de la carrera"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ["codigo", "edificio", "capacidad", "tipo", "activa"]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. A-101, LAB-REDES"}),
            "edificio": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. Edificio Docencia 1"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Capacidad máxima"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["clave", "nombre", "asistencias", "horas_semana", "periodo", "carrera", "activa"]
        widgets = {
            "clave": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. PROG-WEB"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la materia"}),
            "asistencias": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "horas_semana": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "periodo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. 2026-3"}),
            "carrera": forms.Select(attrs={"class": "form-select"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["materia", "profesor", "aula", "grupo", "dia_semana", "hora_inicio", "hora_fin", "periodo", "activo"]
        widgets = {
            "materia": forms.Select(attrs={"class": "form-select"}),
            "profesor": forms.Select(attrs={"class": "form-select"}),
            "aula": forms.Select(attrs={"class": "form-select"}),
            "grupo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. A"}),
            "dia_semana": forms.Select(attrs={"class": "form-select"}),
            "hora_inicio": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "hora_fin": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "periodo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. 2026-3"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["usuario", "materia", "grupo", "periodo", "activa"]
        widgets = {
            "usuario": forms.Select(attrs={"class": "form-select"}),
            "materia": forms.Select(attrs={"class": "form-select"}),
            "grupo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. A"}),
            "periodo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. 2026-3"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
