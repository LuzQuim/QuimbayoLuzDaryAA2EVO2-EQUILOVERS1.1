from django.shortcuts import render
from django.http import JsonResponse
from .models import Instructor

def obtener_instructores(request):
    deporte_id = request.GET.get("deporte_id")
    instructores = Instructor.objects.filter(especialidad_id=deporte_id)
    data = [{"id": inst.id, "nombre": inst.nombre} for inst in instructores]
    return JsonResponse(data, safe=False)


def reservas_home(request):
    return render(request, "reservas/home.html")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm

#@login_required 
def reservas_home(request):
    reservas = Reserva.objects.filter(estudiante=request.user)
    return render(request, "reservas/home.html", {"reservas": reservas})


#@login_required
def nueva_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.estudiante = request.user
            reserva.save()
            return redirect("reservas_home")
    else:
        form = ReservaForm()
    return render(request, "reservas/nueva_reserva.html", {"form": form})


#@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, estudiante=request.user)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("reservas_home")
    else:
        form = ReservaForm(instance=reserva)
    return render(request, "reservas/editar_reserva.html", {"form": form})


#@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, estudiante=request.user)
    if request.method == "POST":
        reserva.delete()
        return redirect("reservas_home")
    return render(request, "reservas/eliminar_reserva.html", {"reserva": reserva})

