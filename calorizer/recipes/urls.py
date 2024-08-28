"""Urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/category/<slug:category_slug>/', views.get_category, name='get_category'),
    path('recipes/type/<slug:type_slug>/', views.get_type, name='get_type'),
    path('recipes/tag/<slug:tag_slug>/', views.get_tag, name='get_tag'),
    path('recipes/mark/<slug:mark_slug>/', views.get_mark, name='get_mark'),
    path('recipes/kind/<slug:kind_slug>/', views.get_kind, name='get_kind'),
    path('recipes/time/<slug:time_slug>/', views.get_time, name='get_time'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
path('recipes/filter/', views.recipes_filter, name='recipes_filter'),
]
