# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnergyDataViewSet

router = DefaultRouter()
router.register('energy-data', EnergyDataViewSet, basename='energydata')



urlpatterns = [
    path('', include(router.urls)),
    # …other patterns…
]
