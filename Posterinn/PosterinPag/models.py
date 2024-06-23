from django.db import models
import datetime
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
    existencias = models.IntegerField()
    
    def __str__(self):
        return self.codigo
    
class boleta(models.Model):
    id=models.AutoField(unique=True, primary_key=True,null=False)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id)

class detalle_boleta(models.Model):
    id = models.ForeignKey(boleta, blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)