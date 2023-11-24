from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo