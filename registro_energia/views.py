from django.shortcuts import render
from .models import RegistroEnergia

def historial(request):
    registros = RegistroEnergia.objects.all().order_by('-fecha')
    return render(request, "registro/historial.html", {"registros": registros})

def graficas(request):
    registros = RegistroEnergia.objects.all().order_by('fecha')
    
    # Prepare data for graph
    labels = []
    consumo_data = []
    costo_data = []
    
    for r in registros:
        if r.rango == 'mes' and r.mes:
            label = r.mes
        else:
            label = r.fecha.strftime("%d/%m/%Y")
            
        labels.append(label)
        consumo_data.append(r.consumo_kwh)
        costo_data.append(r.total)

    return render(request, "registro/graficas.html", {
        "labels": labels,
        "consumo_data": consumo_data,
        "costo_data": costo_data
    })
