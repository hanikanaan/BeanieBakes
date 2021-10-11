from django.shortcuts import render


def base(request):
    return render(request, 'frostingbase.html')


def list(request):
    return render(request, 'ListOfFrostings.html')
