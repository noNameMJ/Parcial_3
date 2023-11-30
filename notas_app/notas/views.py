from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import NotaForm
from .models import Nota


#Vista para ver detalles de un autor
def detalleNota(request, id):
    #Consultar nota
    nota = Nota.objects.get(id=id)           
    if (request.user == nota.ref_user) or request.user.is_staff:
        #Consultar datos de producto
        context = {'nota':nota}
        #Obtener el template
        template = loader.get_template("detalleNota.html")

        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse('No tienes permiso para hacer esto.')

# Vista para crear productos
def crearNota(request):
    if request.user.is_authenticated:
        #Obtener el template
        template = loader.get_template("crearNota.html")
        #Generar Formulario
        if request.method == "POST":
            form = NotaForm(request.POST or None, request.FILES)
            if form.is_valid():
                #obtener datos del formulario
                nota_nueva = form.save(commit=False)
                nota_nueva.ref_user = request.user
                #Guardar Producto
                nota_nueva.save()
                return redirect('index')
        else:
            form = NotaForm()
        #Crear contexto
        context = {}
        context['form'] = form
        #Retornar respuesta http
        return HttpResponse(template.render(context,request))
    else:
        return redirect('login') 

def editarNota(request,id):
    #Obtener el template
    template = loader.get_template("editarNota.html")
    #Buscar 
    nota = get_object_or_404(Nota, id = id)
    if (request.user == nota.ref_user) or request.user.is_staff:
        #formulario que contiene la instancia
        form = NotaForm(request.POST or None, instance = nota)
        if form.is_valid():
            form.save()
            return redirect('index')   
        #Agregar el contexto
        context = {}
        context['form'] = form
        #Retornar respuesta http
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse('No tienes permiso para hacer esto.')

def eliminarNota(request,id):
    #Obtener el template
    template = loader.get_template("eliminarNota.html")
    #Buscar 
    nota = get_object_or_404(Nota, id = id)
    if (request.user == nota.ref_user) or request.user.is_staff:
        if request.method == "POST":
            nota.delete()
            return redirect('index')
        #Agregar el contexto
        context = {}
        #Retornar respuesta http
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse('No tienes permiso para hacer esto.')