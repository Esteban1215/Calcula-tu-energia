from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistroForm(forms.ModelForm):
    username = forms.CharField(
        label="Nombre de usuario", 
        min_length=8, 
        max_length=12, 
        help_text="El nombre de usuario debe tener entre 8 y 12 caracteres."
    )
    email = forms.EmailField(label="Correo electrónico", required=True)
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
