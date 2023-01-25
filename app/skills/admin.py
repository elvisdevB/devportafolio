from django.contrib import admin

#Modelos
from .models import Categoria, Habilidad

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    class Meta:
        model = Categoria

admin.site.register(Categoria, CategoriaAdmin)

class HabilidadAdmin(admin.ModelAdmin):
    class Meta:
        model = Habilidad

admin.site.register(Habilidad, HabilidadAdmin)