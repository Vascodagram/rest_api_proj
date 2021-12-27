from rest_framework import fields, serializers
from .models import Car

class CarListSerializers(serializers.ModelSerializer):
    """List of cars"""

    class Meta:
        model = Car
        fields = '__all__'