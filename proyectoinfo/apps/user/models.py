from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	nombre = models.CharField(max_length=40, null=True, blank=True)
	apellido = models.CharField(max_length=40, null=True, blank=True)
	dni = models.CharField(max_length=8, null=True, blank=True)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	telefono = models.CharField(max_length=15, null=True, blank=True)



