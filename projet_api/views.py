from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProjetSerializers
from .models import Projet


class ProjetViewSet(viewsets.ModelViewSet):  # ModelViewSet est une vue spéciale fournie par Django Rest Framework. Il gère GET et POST
    
    queryset = Projet.objects.all().order_by('id_projet')
    serializer_class = ProjetSerializers

      
