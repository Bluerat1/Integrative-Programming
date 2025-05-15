from django.urls import path
from .views import EnergyDataCreateView

urlpatterns = [
    path('energy-data/', EnergyDataCreateView.as_view(), name='energy-data-create'),
]