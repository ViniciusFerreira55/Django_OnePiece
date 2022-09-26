from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Characters, AkumaNoMi, Navios


def index(request):
    return render(request, 'index.html')


def index(request):
    character = Characters.objects.all()
    akumaNoMi = AkumaNoMi.objects.all()
    dados = {
        'characters': character,
        'akumaNoMis' : akumaNoMi
    }
    return render(request, 'index.html', dados)

def characters(request, character_id):
    character = get_object_or_404(Characters, pk=character_id)
    character_a_ser_exibido = {
        'character' : character
    }
    return render(request, 'info.html', character_a_ser_exibido)

def akumaNoMis(request, akumaNoMi_id):
    akumaNoMi = get_object_or_404(AkumaNoMi, pk=akumaNoMi_id)
    akumaNoMi_a_ser_exibido = {
        'akumaNoMi' : akumaNoMi
    }
    return render(request, 'info2.html', akumaNoMi_a_ser_exibido)

def navios(request, navio_id):
    navio = get_object_or_404(Navios, pk=navio_id)
    navio_a_ser_exibido = {
        'navio' : navio 
    }
    return render(request, 'info3.html', navio_a_ser_exibido)
