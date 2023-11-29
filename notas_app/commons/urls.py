from django.urls import path, include

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('notas/', include('notas.urls')),
]