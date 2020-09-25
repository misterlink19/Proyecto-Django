from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Libro

class CLibrosView(View):
    def get(self, request):
        ListadoLibros = Libro.objects.all()
        context = {'lesles': ListadoLibros}
        return render(request, 'Libreria/Consultas/CLibros.html', context)

class IndexView(View):
    def get(self, request):
        return render(request, 'Libreria/index.html')


