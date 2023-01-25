from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Proyecto")
    descripcion =  models.CharField(max_length=500, verbose_name='Descripción')
    link_demo = models.URLField("Ver Demo", null=True, blank=True)
    foto = models.ImageField(upload_to='proyectos/%Y/%m/%d', null=True, blank=True, verbose_name="Foto Referencia de Aplicacion")

    
    
    def __str__(self):
        return self.nombre

class Contactar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(max_length=100, verbose_name="Correo")
    proyecto = models.CharField(max_length=200, verbose_name="Nombre del Proyecto")
    mensaje = models.CharField(max_length=500, verbose_name="Mensaje")

    def __str__(self):
        return self.proyecto
    