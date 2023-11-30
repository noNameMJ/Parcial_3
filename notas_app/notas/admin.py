from django.contrib import admin
from .models import Nota

class NotaAdmin(admin.ModelAdmin):
    list_display = ('ref_user', 'titulo', 'descripcion', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_creacion', 'ref_user')

admin.site.register(Nota, NotaAdmin)
