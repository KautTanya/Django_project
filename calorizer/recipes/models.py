"""models for recipes"""
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kind(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Time(models.Model):
    duration = models.CharField(max_length=100)  # Наприклад, "<15 хвилин"

    def __str__(self):
        return self.duration


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    categories = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)
    kinds = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    proteins = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fats = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
