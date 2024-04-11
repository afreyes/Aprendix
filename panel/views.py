from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Cursos

def index(request):
    return render(request, "index.html")

def listarcurso(request):
    cursos = Cursos.objects.all()
    datos = {'cursos': cursos}
    return render(request, "crud_usuarios/listarcurso.html", datos)

def agregarcurso(request):
    if request.method == "POST":
        if request.POST.get('nombre') and request.POST.get('descripcion') and request.POST.get('duracion') and request.POST.get('creditos'):
            curso = Cursos()
            curso.nombre = request.POST.get('nombre')
            curso.descripcion = request.POST.get('descripcion')
            curso.duracion = request.POST.get('duracion')
            curso.creditos = request.POST.get('creditos')
            curso.save()
            return redirect('listarcurso')  
    else:
        return render(request, "crud_usuarios/agregarcurso.html")

def actualizarcurso(request, idcurso):
    try:
        curso = Cursos.objects.get(idcurso=idcurso)
        if request.method == 'POST':
            if request.POST.get('nombre') and request.POST.get('descripcion') and request.POST.get('duracion') and request.POST.get('creditos'):
                curso.nombre = request.POST.get('nombre')
                curso.descripcion = request.POST.get('descripcion')
                curso.duracion = request.POST.get('duracion')
                curso.creditos = request.POST.get('creditos')
                curso.save()
                return redirect('listarcurso')  
        else:
            datos = {'curso': curso}
            return render(request, "crud_usuarios/actualizarcurso.html", datos)
    except Cursos.DoesNotExist:
        return HttpResponseNotFound("El curso que intentas actualizar no existe.")

def eliminarcurso(request, idcurso):
    curso = get_object_or_404(Cursos, idcurso=idcurso)
    if request.method == 'POST':
        curso.delete()
        return redirect('listarcurso')  
    else:
        datos = {'curso': curso}
        return render(request, "crud_usuarios/eliminarcurso.html", datos)