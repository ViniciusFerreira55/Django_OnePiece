from django.shortcuts import render, get_object_or_404
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

def characters(request, character_id):
    character = get_object_or_404(Characters, pk=character_id)
    character_a_ser_exibido = {
        'character' : character
    }
    return render(request, 'info.html', character_a_ser_exibido)

def akumasNoMi(request, akumaNoMi_id):
    akumaNoMi = get_object_or_404(AkumaNoMi, pk=akumaNoMi_id)
    akumaNoMi_a_ser_exibido = {
        'akumaNoMi' : akumaNoMi
    }
    return render(request, 'info2.html', akumaNoMi_a_ser_exibido)
