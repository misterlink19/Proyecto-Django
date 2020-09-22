from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.timezone import now

# Create your models here.

#Modelo libro, tiene un metodo que retorna 
# el titulo, año, edicion y precio en formato str
class Libro(models.Model):
    #Caracteriscas propia del libro
    titulo = models.CharField(
        help_text = "Titulo del libro", 
        max_length=150)
    status = models.CharField(
                max_length=27, 
                blank=True, 
                default='Disponible', 
                help_text='Disponibilidad del libro')
    año = models.CharField(
        help_text = "Introduce el año", 
        max_length=50)
    edicion = models.CharField(("Introduce la edicion"), max_length=50)
    precio = models.FloatField(("Introduce el precio"))

    # Caracteristicas foraneas.
    autor = models.ForeignKey(
        'Autor', 
        on_delete=models.CASCADE, 
        null = True)
    
    genero_Id = models.ManyToManyField(
        'Genero',
        help_text = "Seleccione un genero para este libro")
   
    editorial_Id = models.ForeignKey(
        'Editorial', 
        on_delete=models.CASCADE)

    class Meta:
        ordering = ["titulo","autor"]

    def __str__(self):
        return f"{self.titulo} | {self.año} | {self.edicion} | {self.status} | ${self.precio}"


class Autor(models.Model):
    nombre = models.CharField(
        help_text =  "Nombre del autor"
        , max_length=50)
    apellido = models.CharField(
        help_text = "Apellido del autor"
        , max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(
        help_text = "Nombre de la editorial"
        , max_length=127)
    
    def __str__(self):
        return f"{self.nombre}"


class Genero(models.Model):
    nombre = models.CharField(
        help_text = "Genero al que pertenece"
        , max_length=200)
    
    def __str__(self):
        return self.nombre
    

class Lector(models.Model):
    nombre = models.CharField(
        help_text = "Nombre del lector"
        , max_length=50)

    apellido = models.CharField(
        help_text =  "Apellido del lector"
        , max_length=50)
    telefono =models.CharField(  
        help_text = "Numero de telefono"
        , max_length=10)
    direccion = models.CharField(
        help_text =  "Direccion de donde vive" , 
        max_length=127)
    correo = models.EmailField(
        help_text = "Direccion del correo electronico",
        max_length=254)

    def __str__(self):
        return f"{self.nombre} {self.apellido} | {self.telefono[:3]}-{self.telefono[3:6]}-{self.telefono[6:]} | {self.correo} | {self.direccion}"

class Alquiler(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_Alquiler = models.DateField(
        help_text = "Fecha del alquiler", 
        auto_now=False, 
        auto_now_add=False)

    fecha_Entrega = models.DateField(
        help_text = "Fecha de cuando termina el alquiler", 
        auto_now=False, 
        auto_now_add=False)
    precio = models.FloatField(help_text = "Precio del alquiler")

    
    def __str__(self):
        return f"{self.lector} | {self.libro} | {self.fecha_Alquiler} | {self.fecha_Entrega} | {self.precio} "