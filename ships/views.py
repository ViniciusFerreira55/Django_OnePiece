from django.shortcuts import render
from django.http import HttpResponse
from .models import Characters


def index(request):
    return render(request, 'index.html')


def index(request):
    character = Characters.objects.all()
    dados = {
        'characters': character
    }
    return render(request, 'index.html', dados)
