from django.shortcuts import render
from .models import Recipes


def base(request):
    return render(request, 'searchbase.html')


def results(request):
    recipe = Recipes.recipe_name
    instructions = Recipes.recipe
    img = Recipes.image

    return render(request, 'results.html')
