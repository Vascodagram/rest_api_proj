from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.


class Category(models.Model):
    name = models.CharField('Category', max_length=30)

    def __str__(self):
        return f'Category: {self.name}'


class CommentCar(models.Model):
    """Comment"""
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False, default='')
    owner_car = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment: {self.owner_car}, create: {self.created}'


class Car(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    car_brand = models.CharField('brand car', max_length=50)
    model_car = models.CharField('model car', max_length=50)
    vin_code = models.IntegerField('vin_code')
    numberplate = models.CharField('number_plate', max_length=10)
    color_car = models.CharField('Color', max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    owner_car = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.car_brand} {self.model_car} {self.color_car}'

    
