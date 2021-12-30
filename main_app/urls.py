from django.urls import path
from .views import CarListView, CommentList, DetailCarView, UserListView, UserDetailView, CommentDetail

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('car/', CarListView.as_view()),
    path('car-detail/<int:pk>', DetailCarView.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),

]
