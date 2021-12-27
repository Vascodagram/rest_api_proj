from django.db import models
from rest_framework import serializers
# Create your models here.

# class Car(serializers.ModelSerializer):
#     """Model of car"""
#     model_car = 

class Car(models.Model):
    car_brand = models.CharField('brend car', max_length=50)
    model_car = models.CharField('model car', max_length=50)
    vincode = models.IntegerField('vincode')
    numberplate = models.CharField('number_plate', max_length=10)
    color_car = models.CharField('Color', max_length=30)

    def __str__(self) -> str:
        return self.car_brand


    
