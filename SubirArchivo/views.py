from django.shortcuts import render, redirect
from . import models
# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def uploadFile(request):
    if request.method == "POST":
        fileTitle = request.POST["title"]
        archivo = request.FILES["archivo"]

        # Crear una instancia del modelo y asignar el archivo con el nombre único
        document = models.Archivo(title=fileTitle, archivo=archivo)
        document.save()

    return redirect('inicio')


def lista_archivo(request):
    archivos = models.Archivo.objects.all()
    return render(request, "archivos.html", context={"archivos": archivos})
