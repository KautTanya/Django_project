from django.contrib import admin
from recipes.models import Category, Type, Tag, Mark, Kind, Time, Recipe, RecipeIngredient

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Mark)
admin.site.register(Kind)
admin.site.register(Time)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)

