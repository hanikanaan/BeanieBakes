from django.shortcuts import render
from .models import Recipes
import globalvars as gv
from . import searcher


def base(request):
    return render(request, 'searchbase.html')


def results(request):
    input_value = request.GET.get('results', 'This is a default value')
    gv.searchstring = input_value
    context = {'Input value:', input_value}
    searcher.main()
    return render(request, 'results.html', context)
