from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Agrega campos adicionales aquí
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    

class Resenia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenias')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resenias')
    comentario = models.CharField(max_length=200)
    calificacion = models.IntegerField()
    def __str__(self):
        return self.comentario
    

class GameCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):    #Define como representar el objeto cuando se convierte en una cadena de texto.
        return self.name
    
