from django.conf import settings
from django.db import models
from django.utils import timezone


class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    sala = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='monitores'
    )

    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_compra = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo
    
class Clase(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo
