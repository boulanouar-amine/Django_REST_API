from django.urls import include, path
from rest_framework import routers
from GestionFilliere.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'departement',DepartementViewSet)
router.register(r'filiere',FiliereViewSet)
router.register(r'etudiant',EtudiantViewSet)
router.register(r'enseignant',EnseignantViewSet)
router.register(r'classe',ClasseViewSet)
router.register(r'elementmodule',ElementmoduleViewSet)
router.register(r'module',ModuleViewSet)
router.register(r'infosuretudiant',InfosuretudiantViewSet)
router.register(r'naturecours',NaturecoursViewSet)
router.register(r'reservation',ReservationViewSet)



urlpatterns = [
    path('',include(router.urls)),
]

