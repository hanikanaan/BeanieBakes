from django import forms
from .models import Recipes


class RecipeForm(forms.Form):
    recipe_search = forms.CharField(label='', max_length=64)
