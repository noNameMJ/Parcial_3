from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from notas.models import Nota
from .forms import NewUserForm

# Create your views here.
def index(request):
    notas_list = Nota.objects.all()
    #Configurar paginación cada 10 productos
    paginator = Paginator(notas_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context,request))

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))