from django.shortcuts import render
from .models import RegistroEnergia

def historial(request):
    registros = RegistroEnergia.objects.all().order_by('-fecha')
    return render(request, "registro/historial.html", {"registros": registros})
