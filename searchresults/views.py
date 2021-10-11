from django.shortcuts import render


def base(request):
    return render(request, 'searchbase.html')


def results(request):
    return render(request, 'results.html')
