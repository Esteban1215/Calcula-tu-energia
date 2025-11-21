from django.shortcuts import render
from .forms import CalculadoraForm
from registro_energia.models import RegistroEnergia
from datetime import datetime

VALOR_KWH = 220  # $220 por kWh

def calcular(request):
    resultado = None

    if request.method == "POST":
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            consumo = form.cleaned_data["consumo_kwh"]
            rango = form.cleaned_data["rango"]
            mes = form.cleaned_data.get("mes")

            # cálculo
            total = consumo * VALOR_KWH

            # Guardar en el historial
            RegistroEnergia.objects.create(
                consumo_kwh=consumo,
                rango=rango,
                mes=mes,
                total=total,
                fecha=datetime.now()
            )

            resultado = total
    else:
        form = CalculadoraForm()

    return render(request, "calculadora/calcular.html", {
        "form": form,
        "resultado": resultado
    })
