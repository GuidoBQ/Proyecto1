from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola munbdo!</h1>")

def minombrees(self, nombre):
    documentodetexto = f"mi nombre es <h1>{nombre}</h1>"
    return HttpResponse(documentodetexto)

def probandoTemplate(self):
    nombre = "Guido"
    apellido = "Ormeño"
    namelist = ["Julieta", "Jennifer", "Lucas", "Matias"]
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    #miHtml = open("D:/Users/guido/Documents/Coder/PythonProyecto1/Proyecto1/Proyecto1/Plantillas/template1.html")
    #miHtml = loader.get_template("template1.html")
    plantilla = loader.get_template("template1.html")
    #miHtml.close()
    #miContext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
