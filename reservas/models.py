from django.db import models
from django.contrib.auth.models import User

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Reserva(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.estudiante} - {self.deporte} con {self.instructor} el {self.fecha} a las {self.hora}"

