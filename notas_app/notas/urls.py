from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('crear/',views.crearNota, name='crearNotas'),
    path('detalle/<id>/',views.detalleNota, name='detalleNotas'),
    path('editar/<id>/',views.editarNota, name='editarNotas'),
    path('borrar/<id>/',views.eliminarNota, name='eliminarNotas')
]