from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from usuarios.models import Usuario

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario o Correo Electrónico",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu usuario o correo",
            "autofocus": "autofocus",
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "••••••••",
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if identifier and password:
            lookup_username = identifier.strip()
            if "@" in lookup_username:
                try:
                    user_obj = Usuario.objects.get(email__iexact=lookup_username)
                    lookup_username = user_obj.username
                except (Usuario.DoesNotExist, Usuario.MultipleObjectsReturned):
                    pass

            self.user_cache = authenticate(self.request, username=lookup_username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Credenciales inválidas. Verifica tu usuario y contraseña.")
            if not self.user_cache.activo:
                raise forms.ValidationError("Esta cuenta de usuario se encuentra inactiva.")

        return cleaned_data

    def get_user(self):
        return self.user_cache


class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password",
        }),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password",
        }),
    )

    class Meta:
        model = Usuario
        fields = [
            "nombre",
            "apaterno",
            "amaterno",
            "matricula",
            "email",
            "whatsapp",
            "grupo",
            "username",
        ]
        labels = {
            "nombre": "Nombre(s)",
            "apaterno": "Apellido paterno",
            "amaterno": "Apellido materno",
            "matricula": "Matrícula",
            "email": "Correo electrónico",
            "whatsapp": "WhatsApp / teléfono",
            "grupo": "Grupo",
            "username": "Nombre de usuario",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apaterno": forms.TextInput(attrs={"class": "form-control"}),
            "amaterno": forms.TextInput(attrs={"class": "form-control"}),
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "autocomplete": "email",
            }),
            "whatsapp": forms.TextInput(attrs={"class": "form-control"}),
            "grupo": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "autocomplete": "username",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ("nombre", "apaterno", "amaterno", "matricula"):
            self.fields[field_name].required = True
        self.order_fields([
            "nombre",
            "apaterno",
            "amaterno",
            "matricula",
            "email",
            "whatsapp",
            "grupo",
            "username",
            "password1",
            "password2",
        ])

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if Usuario.objects.filter(username__iexact=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        if Usuario.objects.filter(email__iexact=email).exists():
            raise ValidationError("Ya existe una cuenta con este correo electrónico.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Las contraseñas no coinciden.")
        elif password1:
            user = Usuario(
                username=cleaned_data.get("username", ""),
                email=cleaned_data.get("email", ""),
                nombre=cleaned_data.get("nombre", ""),
                apaterno=cleaned_data.get("apaterno", ""),
                amaterno=cleaned_data.get("amaterno", ""),
            )
            try:
                validate_password(password1, user)
            except ValidationError as error:
                self.add_error("password1", error)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
