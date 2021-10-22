from django.shortcuts import render


def base(request):
    return render(request, 'cookiesbase.html')


def list(request):
    return render(request, 'cookieslist.html')
