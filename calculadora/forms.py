from django import forms

class CalculadoraForm(forms.Form):
    consumo_kwh = forms.FloatField(label="Consumo en kWh")
    rango = forms.ChoiceField(
        choices=[("semana", "Semana"), ("mes", "Mes")],
        label="Seleccione un rango"
    )
    mes = forms.ChoiceField(
        choices=[
            ("", "Seleccione un mes"),
            ("Enero", "Enero"), ("Febrero", "Febrero"), ("Marzo", "Marzo"),
            ("Abril", "Abril"), ("Mayo", "Mayo"), ("Junio", "Junio"),
            ("Julio", "Julio"), ("Agosto", "Agosto"), ("Septiembre", "Septiembre"),
            ("Octubre", "Octubre"), ("Noviembre", "Noviembre"), ("Diciembre", "Diciembre")
        ],
        label="Mes",
        required=False
    )
