from .models import Task
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Task)

def registrar_cambio(sender, instance, created, **kwargs):
    
    if created:
        print(f"Tarea creada: {instance.title}")
    else:
        print(f"Tarea Actualizada: {instance.title}")