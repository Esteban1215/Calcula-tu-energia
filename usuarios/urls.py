from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_usuario, name="login_root"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_usuario, name="login"),
    path("logout/", views.logout_usuario, name="logout"),
]
