from django.db import models

class RegistroEnergia(models.Model):
    consumo_kwh = models.FloatField()
    rango = models.CharField(max_length=20)  # semana o mes
    total = models.FloatField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.rango} - {self.total}"
