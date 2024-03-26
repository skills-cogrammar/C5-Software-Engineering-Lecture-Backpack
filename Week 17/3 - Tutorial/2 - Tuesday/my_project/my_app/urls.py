from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('users/', views.index),
    path('register/', views.register),
    path('register/register_user', views.register_user),
]