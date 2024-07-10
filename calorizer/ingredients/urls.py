"""Urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ingredients_list, name='ingredients_list'),

]
