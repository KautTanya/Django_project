"""models for recipes"""
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Kind(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Time(models.Model):
    duration = models.CharField(max_length=100)  # Наприклад, "<15 хвилин"
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.duration


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    ingredients = models.ManyToManyField('ingredients.Ingredient', related_name='recipes')
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='recipes')
    types = models.ManyToManyField(Type, blank=True, related_name='recipes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipes')
    marks = models.ManyToManyField(Mark, blank=True, related_name='recipes')
    kinds = models.ManyToManyField(Kind, blank=True, related_name='recipes')
    times = models.ManyToManyField(Time, blank=True, related_name='recipes')
    calories = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    proteins = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fats = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.quantity} of {self.ingredient.name} in {self.recipe.name}'
