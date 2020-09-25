from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'Libreria/index.html')

from .models import Libro

class CLibrosView(View):
    def get(self, request):
        context = {'libros': Libro.objects.all()}
        return render(request, 'Libreria/CLibros.html', context)