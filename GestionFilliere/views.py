from rest_framework import viewsets
from GestionFilliere.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


class FiliereViewSet(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer


class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer


class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ElementmoduleViewSet(viewsets.ModelViewSet):
    queryset = Elementmodule.objects.all()
    serializer_class = ElementmoduleSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class InfosuretudiantViewSet(viewsets.ModelViewSet):
    queryset = Infosuretudiant.objects.all()
    serializer_class = InfosuretudiantSerializer


class NaturecoursViewSet(viewsets.ModelViewSet):
    queryset = Naturecours.objects.all()
    serializer_class = Naturecoursserializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
