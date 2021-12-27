from django.urls import path
from .views import CarListView

urlpatterns = [
    path('car/', CarListView.as_view()),
]