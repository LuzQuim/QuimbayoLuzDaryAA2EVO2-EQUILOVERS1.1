from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservas_home, name='reservas_home'),
    path('', views.reservas_home, name='reservas_home'),
    path('nueva/', views.nueva_reserva, name='nueva_reserva'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('obtener-instructores/', views.obtener_instructores, name='obtener_instructores'),
    
]
