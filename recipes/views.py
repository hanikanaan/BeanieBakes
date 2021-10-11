from django.shortcuts import render


def base(request):
    return render(request, 'recipesbase.html')


def list(request):
    return render(request, 'recipelist.html')
