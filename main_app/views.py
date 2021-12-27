from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarListSerializers
# Create your views here.

class CarListView(APIView):
    """List of cars"""
    def get(self, request):
        car = Car.objects.all()
        serializers = CarListSerializers(car, many=True)
        return Response(serializers.data)
