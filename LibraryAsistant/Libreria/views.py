from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Libro, Alquiler, Autor,Genero, Editorial, Lector

# Create your views here.
class IndexView(View):
    def get(self,request):
        context = {'libros': Libro.objects.all()}
        return render(request, 'libreria/index.html', context)
