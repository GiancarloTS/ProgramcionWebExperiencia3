from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    
    codigo = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/',null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    
    def __str__(self):
        return self.nombre
# Create your models here.
