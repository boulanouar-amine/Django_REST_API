from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','is_staff']



class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class ElementmoduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elementmodule
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class InfosuretudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infosuretudiant
        fields = '__all__'

class Naturecoursserializer(serializers.ModelSerializer):
    class Meta:
        model = Naturecours
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class Salleserializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'

class Semaineserializer(serializers.ModelSerializer):
    class Meta:
        model = Semaines
        fields = '__all__'

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'