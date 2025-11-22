from django.shortcuts import render, redirect
from .models import RegistroEnergia

from django.db.models import Sum

def historial(request):
    registros = RegistroEnergia.objects.all().order_by('-fecha')
    
    total_general = registros.aggregate(Sum('total'))['total__sum'] or 0
    total_semana = registros.filter(rango='semana').aggregate(Sum('total'))['total__sum'] or 0
    total_mes = registros.filter(rango='mes').aggregate(Sum('total'))['total__sum'] or 0

    return render(request, "registro/historial.html", {
        "registros": registros,
        "total_general": total_general,
        "total_semana": total_semana,
        "total_mes": total_mes
    })

def graficas(request):
    registros = RegistroEnergia.objects.all().order_by('fecha')
    
    # Prepare data for monthly graph
    labels_mes = []
    consumo_mes = []
    costo_mes = []

    # Prepare data for weekly graph
    labels_semana = []
    consumo_semana = []
    costo_semana = []
    
    for r in registros:
        if r.rango == 'mes':
            label = r.mes if r.mes else r.fecha.strftime("%d/%m/%Y")
            labels_mes.append(label)
            consumo_mes.append(r.consumo_kwh)
            costo_mes.append(r.total)
        elif r.rango == 'semana':
            label = r.semana if r.semana else r.fecha.strftime("%d/%m/%Y")
            labels_semana.append(label)
            consumo_semana.append(r.consumo_kwh)
            costo_semana.append(r.total)

    return render(request, "registro/graficas.html", {
        "labels_mes": labels_mes,
        "consumo_mes": consumo_mes,
        "costo_mes": costo_mes,
        "labels_semana": labels_semana,
        "consumo_semana": consumo_semana,
        "costo_semana": costo_semana
    })

def limpiar_historial(request):
    if request.method == "POST":
        RegistroEnergia.objects.all().delete()
    return redirect('historial')
