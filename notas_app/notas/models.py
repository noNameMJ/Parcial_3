from django.db import models
from django.contrib.auth.models import User

class Nota(models.Model):
    """
    Modelo que representa los productos que son vendidos en la tienda, 
    tiene asociada una categoria (que tambien esta asociada a un animal)
    y un estado
    """
    ref_user = models.ForeignKey(User,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    fecha_creacion = models.DateTimeField(auto_now=True)


