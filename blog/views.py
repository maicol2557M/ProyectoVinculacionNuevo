from django.shortcuts import render
from .models import Articulo

def lista_Articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})
