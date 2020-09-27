from django.contrib import admin
from .models import Libro,Lector, Autor, Genero, Alquiler, Editorial

# Register your models here.
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Alquiler)
admin.site.register(Editorial)