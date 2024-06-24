from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
# Create your models here.


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