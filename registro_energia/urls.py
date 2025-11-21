from django.urls import path
from . import views

urlpatterns = [
    path("", views.historial, name="historial"),
    path("graficas/", views.graficas, name="graficas"),
]
