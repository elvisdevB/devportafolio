from django.db import models

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombres")
    apellido = models.CharField(max_length=100, verbose_name="Apellidos")
    correo = models.EmailField(max_length=300, verbose_name="Correo")
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', null=True, blank=True, verbose_name="Foto de Perfil")
    lugar_residencia = models.CharField(max_length=50, verbose_name="Lugar de Residencia")
    cargo = models.CharField(max_length=50, verbose_name="Cargo que ocupa")
    instagram = models.URLField('Instagram', null=True, blank=True)
    linkedin = models.URLField('Linkedin', null=True, blank=True)
    telegram = models.URLField('Telegram', null=True)
    whatsaap = models.URLField('Whatssap', null=True)
    github = models.URLField('GitHub', null=True, blank=True)
    anos_trabajo = models.IntegerField(verbose_name="Años de Trabajo")
    proyectos_completados = models.IntegerField(verbose_name="Proyectos Completados")
    clientes_satisfechos = models.IntegerField(verbose_name="Clientes Satisfechos")
    cv = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True, verbose_name="Curriculum Vitae")
    telefono = models.CharField(max_length=16, verbose_name="Telefono", null=True)

    def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def __str__(self):
        return self.nombre_completo()


    