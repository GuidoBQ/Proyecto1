from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.forms import formSetEstudiante
from AppCoder.models import Estudiante


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=data["nombre"],apellido=data["apellido"], email = data["email"])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = formSetEstudiante()
        return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario})

def getEstudiante(request):
    return render (request, "AppCoder/getEstudiante.html")

def buscarEstudiante(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre= nombre)
        return render(request, "AppCoder/getEstudiante.html", {"estudiantes":estudiantes})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)
# Create your views here.

