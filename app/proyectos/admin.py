from django.contrib import admin

#Modelo
from .models import Proyecto, Contactar

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    class Meta:
        model = Proyecto

admin.site.register(Proyecto, ProyectoAdmin)

class ContactoAdmin(admin.ModelAdmin):
    class Meta:
        model = Contactar

admin.site.register(Contactar, ContactoAdmin)
