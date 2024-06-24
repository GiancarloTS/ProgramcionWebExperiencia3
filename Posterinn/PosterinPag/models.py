from django.db import models
import datetime
from django.contrib.auth.models import User 
from django.db.models.signals import post_save

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario') #OnetoOne realacion de uno a uno con la tabla User
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id'] #orden por registro recientemente creado

    def __str__(self):
        return self.user.username

def creacion_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)#cuando creo un usuario creo el perfil

def guardado_perfil_usuario(sender, instance, **kwargs):#Con kwargs los argumentos pueden tener una longitud variable, ene ste caso un nro indefinido de users
    instance.profile.save()

post_save.connect(creacion_perfil_usuario, sender=User)
post_save.connect(guardado_perfil_usuario, sender=User)#Conectamos el usuario con el perfil 

class Categoria(models.Model):
    nombre = models.CharField(max_length=210)
    
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    
    codigo = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
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
    
