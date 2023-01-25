from django.urls import path

#Models
from .views import VistaPortafolio

urlpatterns = [
    path('', VistaPortafolio.as_view(), name='index'),
]
