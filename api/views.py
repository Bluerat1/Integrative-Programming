from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import EnergyData
from .serializers import EnergyDataSerializer

class EnergyDataCreateView(generics.CreateAPIView):
    queryset = EnergyData.objects.all()
    serializer_class = EnergyDataSerializer
    permission_classes = [IsAuthenticated]