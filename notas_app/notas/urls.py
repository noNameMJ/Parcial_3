from django.contrib import admin
from django.urls import path, include

from . import views
from commons.views import index

urlpatterns = [
    #ruta, vista, nombre interno
    path('admin/', admin.site.urls),
    path('',index, name='index'),
]