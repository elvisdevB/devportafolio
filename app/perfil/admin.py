from django.contrib import admin

#Modelo
from app.perfil.models import Perfil
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    class Meta:
        model = Perfil

admin.site.register(Perfil, PerfilAdmin)
