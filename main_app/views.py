from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, CommentCar, Category
from .serializers import CommentSerializer, CarDetailSerializers, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class UserListView(generics.ListAPIView):
    """View detailed list of all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """View detailed one user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarListView(generics.ListCreateAPIView):
    """View detailed list of all cars"""
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializers
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner_car=self.request.user)


class DetailCarView(generics.RetrieveDestroyAPIView):
    """View detailed one car"""
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializers
    permission_classes = (IsOwnerOrReadOnly, )


class CommentList(generics.ListCreateAPIView):
    queryset = CommentCar.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner_car=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentCar.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )
