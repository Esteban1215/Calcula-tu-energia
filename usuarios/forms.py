from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistroForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico", required=True, help_text="No es necesario un correo real.")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repetir contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        labels = {
            "username": "Nombre de usuario",
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
