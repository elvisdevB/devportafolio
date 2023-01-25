from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib import messages

#Response
from  django.http import JsonResponse

#Formulario
from app.proyectos.forms import ContactarForm

#Modelos
from app.perfil.models import Perfil
from app.skills.models import Habilidad, Categoria
from app.proyectos.models import Proyecto
from app.proyectos.models import Contactar

class VistaPortafolio(ListView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        
        #Perfil Usuario

        perfil = Perfil.objects.get(nombre="Elvis")
        
        #Habilidades
        frontend = Categoria.objects.get(nombre="Frontend Developer")
        frontend_habilidad = Habilidad.objects.filter(id_categoria = Categoria.objects.get(nombre = "Frontend Developer"))
        
        backend = Categoria.objects.get(nombre="Backend Developer")
        backend_habilidad = Habilidad.objects.filter(id_categoria = Categoria.objects.get(nombre = "Backend Developer"))
        
        #Proyectos
        proyectos = Proyecto.objects.all()
        
        context = {
            'frontend' : frontend,
            'frontend_habilidad' : frontend_habilidad,
            'backend' : backend,
            'backend_habilidad' : backend_habilidad,
            'perfil' : perfil,
            'proyectos': proyectos
        }

        return render(request, 'layout.html', context)
    
    def post(self, request, *args, **kwargs):
        data={}
        with transaction.atomic():
            contacto = Contactar()
            contacto.nombre = request.POST.get('nombre')
            contacto.correo = request.POST.get('email')
            contacto.proyecto = request.POST.get('project')
            contacto.mensaje = request.POST.get('mensaje')
            contacto.save()
            messages.success(request, "Se ha enviado mensaje con Exito")
        
        return redirect('/')