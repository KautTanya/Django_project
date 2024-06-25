"""models for ingredients"""
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)  # Калорійність на 100 гр
    proteins = models.DecimalField(max_digits=6, decimal_places=2)  # Кількість білків на 100 гр
    fats = models.DecimalField(max_digits=6, decimal_places=2)  # Кількість жирів на 100 гр
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)  # Кількість вуглеводів на 100 гр
    unit = models.CharField(max_length=50, default='grams', blank=True)  # Одиниця виміру
    image = models.ImageField(upload_to='ingredients/', blank=True, null=True)  # Зображення інгредієнта

    def __str__(self):
        return self.name
