from django.urls import include, path
from rest_framework import routers
from GestionFilliere.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'departement', DepartementViewSet)
router.register(r'filiere', FiliereViewSet)
router.register(r'enseignant', EnseignantViewSet)
router.register(r'etudiant', EtudiantViewSet)
router.register(r'semestre', SemestreViewSet)
router.register(r'module', ModuleViewSet)
router.register(r'elementmodule', ElementmoduleViewSet)
router.register(r'naturecours', NaturecoursViewSet)
router.register(r'classe', ClasseViewSet)
router.register(r'classe_etudiant', ClassEtudiantViewSet)
router.register(r'charge_horaire_enseignant', ChargeHoraireEnseignantViewSet)
router.register(r'session', SessionViewSet)
router.register(r'infosuretudiant', InfosuretudiantViewSet)
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
