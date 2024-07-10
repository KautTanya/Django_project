"""ingredients"""
from django.shortcuts import render
from .models import Ingredient


def ingredients_list(request):
    """example"""
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/ingredients_list.html', {'ingredients': ingredients})
