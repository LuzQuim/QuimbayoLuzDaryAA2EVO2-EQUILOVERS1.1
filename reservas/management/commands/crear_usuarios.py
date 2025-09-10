from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = "Crea usuarios de prueba con roles (admin, trabajador, estudiante)"

    def handle(self, *args, **kwargs):
        # Crear grupos si no existen
        trabajador_group, _ = Group.objects.get_or_create(name="Trabajador")
        estudiante_group, _ = Group.objects.get_or_create(name="Estudiante")

        # Crear superusuario admin
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("✅ Admin creado: usuario=admin, pass=admin123"))

        # Crear usuario trabajador
        if not User.objects.filter(username="trabajador1").exists():
            trabajador = User.objects.create_user("trabajador1", password="trabajador123")
            trabajador.groups.add(trabajador_group)
            self.stdout.write(self.style.SUCCESS("✅ Trabajador creado: usuario=trabajador1, pass=trabajador123"))

        # Crear usuario estudiante
        if not User.objects.filter(username="estudiante1").exists():
            estudiante = User.objects.create_user("estudiante1", password="estudiante123")
            estudiante.groups.add(estudiante_group)
            self.stdout.write(self.style.SUCCESS("✅ Estudiante creado: usuario=estudiante1, pass=estudiante123"))
