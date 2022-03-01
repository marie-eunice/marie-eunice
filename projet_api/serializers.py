from rest_framework import serializers

from .models import Projet

class ProjetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = ('id_projet', 'nom', 'description', 'date_debut', 'date_fin', 'id_academicien')
