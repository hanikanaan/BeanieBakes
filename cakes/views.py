from django.shortcuts import render


def base(request):
    return render(request, 'cakesbase.html')

def list(request):
    return render(request, 'cakeslist.html')
