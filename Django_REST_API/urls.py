from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

from GestionFilliere import urls as GestionFilliere_urls


urlpatterns = [
    path('',include(GestionFilliere_urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]

