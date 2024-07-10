"""models for menu"""
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)  # Назва меню, наприклад "Тижневе меню" або "Різдвяне меню"
    description = models.TextField(blank=True, null=True)  # Опис меню
    breakfast = models.ManyToManyField('recipes.Recipe', related_name='breakfast_menus', blank=True)
    snack = models.ManyToManyField('recipes.Recipe', related_name='snack_menus', blank=True)
    lunch = models.ManyToManyField('recipes.Recipe', related_name='lunch_menus', blank=True)
    dinner = models.ManyToManyField('recipes.Recipe', related_name='dinner_menus', blank=True)
    total_calories = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_proteins = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_fats = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)  # Дата створення меню
    last_modified = models.DateTimeField(auto_now=True)  # Останні зміни

    def __str__(self):
        return self.name

