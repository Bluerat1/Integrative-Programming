from rest_framework import viewsets, permissions
from .models import EnergyData
from .serializers import EnergyDataSerializer

class EnergyDataViewSet(viewsets.ModelViewSet):
    """
    GET  /api/energy-data/       → list
    POST /api/energy-data/       → create
    (plus retrieve/update/delete at /api/energy-data/{pk}/)
    """
    queryset = EnergyData.objects.all()
    serializer_class = EnergyDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
