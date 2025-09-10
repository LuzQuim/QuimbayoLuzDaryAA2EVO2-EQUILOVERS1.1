def home(request):
    return render(request, "index_django.html")

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        rol = request.POST["rol"]  # 👈 nuevo: leer el rol del formulario

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirigir según el rol seleccionado
            if rol == "admin":
                return redirect("admin_dashboard")
            elif rol == "trabajador":
                return redirect("trabajador_dashboard")
            else:
                return redirect("cliente_dashboard")

        else:
            return render(request, "login.html", {"error": "Usuario o contraseña incorrectos"})

    return render(request, "login.html")



@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

@login_required
def trabajador_dashboard(request):
    return render(request, "trabajador_dashboard.html")

@login_required
def cliente_dashboard(request):
    return render(request, "cliente_dashboard.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("login")
