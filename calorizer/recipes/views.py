"""Recipes"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category, Type, Tag, Mark, Kind, Time
from recipes.forms import RecipeForm


def recipes_list(request):
    """List all recipes"""
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories,
        'types': types,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/recipes_list.html', context)


def get_category(request, category_slug):
    """Get recipes by category slug"""
    category = get_object_or_404(Category, slug=category_slug)
    recipes = Recipe.objects.filter(categories=category)
    categories = Category.objects.all()
    types = Type.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories,
        'category': category,
        'types': types,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/category.html', context)


def get_type(request, type_slug):
    """Get recipes by type slug"""
    type = get_object_or_404(Type, slug=type_slug)
    recipes = Recipe.objects.filter(types=type)
    types = Type.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'types': types,
        'type': type,
        'categories': categories,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/type.html', context)


def get_tag(request, tag_slug):
    """Get recipes by tag slug"""
    tag = get_object_or_404(Tag, slug=tag_slug)
    recipes = Recipe.objects.filter(tags=tag)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    types = Type.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'tag': tag,
        'types': types,
        'categories': categories,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/tag.html', context)


def get_mark(request, mark_slug):
    """Get recipes by mark slug"""
    mark = get_object_or_404(Mark, slug=mark_slug)
    recipes = Recipe.objects.filter(marks=mark)
    types = Type.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'types': types,
        'mark': mark,
        'categories': categories,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/mark.html', context)


def get_kind(request, kind_slug):
    """Get recipes by kind slug"""
    kind = get_object_or_404(Kind, slug=kind_slug)
    recipes = Recipe.objects.filter(kinds=kind)
    types = Type.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'types': types,
        'kind': kind,
        'categories': categories,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/kind.html', context)


def get_time(request, time_slug):
    """Get recipes by time slug"""
    time = get_object_or_404(Time, slug=time_slug)
    recipes = Recipe.objects.filter(times=time)
    types = Type.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    marks = Mark.objects.all()
    kinds = Kind.objects.all()
    times = Time.objects.all()
    context = {
        'recipes': recipes,
        'types': types,
        'time': time,
        'categories': categories,
        'tags': tags,
        'marks': marks,
        'kinds': kinds,
        'times': times,
    }
    return render(request, 'recipes/time.html', context)


def recipe_detail(request, slug):
    """View recipe detail by slug"""
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def add_recipe(request):
    """Add a new recipe"""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})


def recipes_filter(request):
    """Filter recipes based on query parameters"""
    categories = request.GET.getlist('categories')
    types = request.GET.getlist('types')
    tags = request.GET.getlist('tags')
    marks = request.GET.getlist('marks')
    kinds = request.GET.getlist('kinds')
    times = request.GET.getlist('times')

    recipes = Recipe.objects.all()

    if categories:
        recipes = recipes.filter(categories__slug__in=categories)
    if types:
        recipes = recipes.filter(types__slug__in=types)
    if tags:
        recipes = recipes.filter(tags__slug__in=tags)
    if marks:
        recipes = recipes.filter(marks__slug__in=marks)
    if kinds:
        recipes = recipes.filter(kinds__slug__in=kinds)
    if times:
        recipes = recipes.filter(times__slug__in=times)

    context = {
        'recipes': recipes,
        'categories': Category.objects.all(),
        'types': Type.objects.all(),
        'tags': Tag.objects.all(),
        'marks': Mark.objects.all(),
        'kinds': Kind.objects.all(),
        'times': Time.objects.all(),
    }
    return render(request, 'recipes/recipes_filter.html', context)