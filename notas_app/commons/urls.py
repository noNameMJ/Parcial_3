from django.urls import path, include

from . import views
from notas.views import crearNota,detalleNota,editarNota,eliminarNota

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('crear/',crearNota, name='crearNota'),
    path('detalle/<id>/',detalleNota, name='detalleNota'),
    path('editar/<id>/',editarNota, name='editarNota'),
    path('borrar/<id>/',eliminarNota, name='eliminarNota')
]