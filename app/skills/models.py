from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):

    nivelopciones = {
        ('basico','Basico'),
        ('intermedio','Intermedio'),
        ('avanzado','Avanzado')
    }

    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name="Categoria de Habilidad")
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Habilidad")
    nivel = models.CharField(max_length=15,choices=nivelopciones, default='Basico',null=False)

    def __str__(self):
        return self.nombre
    