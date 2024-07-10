"""Recipes"""
from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipes_list(request):
    """example"""
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    """example"""
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
