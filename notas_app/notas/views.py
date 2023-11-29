from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import NotaForm
from .models import Nota


#Vista para ver detalles de un autor
def detalleProducto(request, id):
    #Consultar nota
    nota = Nota.objects.get(id=id)           

    #Consultar datos de producto
    context = {'nota':nota}
    #Obtener el template
    template = loader.get_template("detalleNota.html")

    return HttpResponse(template.render(context,request))

# Vista para crear productos
def crearProducto(request):
    #Obtener el template
    template = loader.get_template("crearNota.html")
    #Generar Formulario
    if request.method == "POST":
        form = NotaForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            nota_nueva = form.save(commit=False)
            #Asignar fecha de creación
            nota_nueva.fecha_creacion = datetime.now()
            #Guardar Producto
            nota_nueva.save()
            return redirect('./commons/templates/index.html')
    else:
        form = NotaForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def editarNota(request,id):
    #Obtener el template
    template = loader.get_template("editarNota.html")
    #Buscar Producto
    obj = get_object_or_404(Nota, id = id)
    #formulario que contiene la instancia
    form = NotaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('./commons/templates/index.html')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def eliminarNota(request,id):
    #Obtener el template
    template = loader.get_template("eliminarNota.html")
    #Buscar el producto
    obj = get_object_or_404(Nota, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('./commons/templates/index.html')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))