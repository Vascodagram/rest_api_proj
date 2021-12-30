from rest_framework import fields, serializers, generics
from .models import Car, CommentCar, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cars', 'model_car', )


class CarDetailSerializers(serializers.ModelSerializer):
    """Detail serializer of model Car"""
    owner_car = serializers.ReadOnlyField(source='owner_car.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner_car = serializers.ReadOnlyField(source='owner_car.username')

    class Meta:
        model = CommentCar
        fields = '__all__'

