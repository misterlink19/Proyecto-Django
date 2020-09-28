from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Libro, Alquiler, Autor,Genero, Editorial, Lector
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class IndexView(View):
    def get(self,request):
        context = {'libros': Libro.objects.all()}
        return render(request, 'libreria/index.html', context)

class LibroIndex(View):
    def get(self, request):
        context = {'libros': Libro.objects.all()}
        return render(request,'libreria/libros.html',context)

class LibroNuevo(CreateView):
     model = Libro
     fields = '__all__'
     success_url = '/libros'

class LibroEditar(UpdateView):
     model = Libro
     fields = '__all__'
     success_url = '/libros'

class LibroEliminar(DeleteView):
     model = Libro
     fields = '__all__'
     success_url = '/libros'

class AlquilerIndex(View):
    def get(self, request):
        context = {'alquilers': Alquiler.objects.all()}
        return render(request,'libreria/alquiler.html',context)

class AlquilerNuevo(CreateView):
     model = Alquiler
     fields = '__all__'
     success_url = '/alquilers'

class AlquilerEditar(UpdateView):
     model = Alquiler
     fields = '__all__'
     success_url = '/alquilers'

class AlquilerEliminar(DeleteView):
     model = Alquiler
     fields = '__all__'
     success_url = '/alquilers'