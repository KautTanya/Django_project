"""create recipe"""
from recipes.models import Recipe
from django.forms import ModelForm


class RecipeForm(ModelForm):
    """form"""
    class Meta:
        """Meta"""
        model = Recipe
        fields = '__all__'
