from django.contrib import admin
from .models import Car, CommentCar, Category
# Register your models here.

admin.site.register(Car)
admin.site.register(CommentCar)
admin.site.register(Category)
