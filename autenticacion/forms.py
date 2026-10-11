from django import forms
from django.contrib.auth import authenticate
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
