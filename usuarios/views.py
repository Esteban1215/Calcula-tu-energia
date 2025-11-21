from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            return redirect("login")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})


def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)

            if user:
                login(request, user)
                return redirect("/")
    else:
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form})


def logout_usuario(request):
    logout(request)
    return redirect("login")
