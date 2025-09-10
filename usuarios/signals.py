from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Solo ejecutar si estamos en la app "usuarios"
    if sender.name == "usuarios":
        for rol in ["Administrador", "Trabajador", "Cliente"]:
            Group.objects.get_or_create(name=rol)
