from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    pais = models.CharField(max_length=30)
