"""Urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
