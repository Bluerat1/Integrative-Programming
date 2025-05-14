from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Device, SensorReading
from .serializers import SensorReadingSerializer

class SensorReadingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        device_name = request.data.get('device_name')
        if not device_name:
            return Response({'error': 'device_name is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            device = Device.objects.get(name=device_name, user=request.user)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SensorReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(device=device)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)