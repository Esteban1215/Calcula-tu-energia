from django import forms

class CalculadoraForm(forms.Form):
    consumo_kwh = forms.FloatField(label="Consumo en kWh")
    rango = forms.ChoiceField(
        choices=[("semana", "Semana"), ("mes", "Mes")],
        label="Seleccione un rango"
    )
