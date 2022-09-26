from django.contrib import admin
from .models import Characters, AkumaNoMi, Navios
# Register your models here.

class characters_display(admin.ModelAdmin):
    list_display = ('id', 'nome_personagem', 'recompensa_personagem', 'tripulacao_personagem', 'akumaNoMi_personagem', 'descricao_personagem', 'foto', 'fotog')
admin.site.register(Characters, characters_display)

class akumaNoMi_display(admin.ModelAdmin):
    list_display = ('id', 'nome_akuma', 'tipo_akuma', 'descricao_akuma', 'foto_akuma')
admin.site.register(AkumaNoMi, akumaNoMi_display)

class navio_display(admin.ModelAdmin):
    list_display = ('id', 'nome_navio', 'nome_capitao', 'descricao_navio', 'foto_navio')
admin.site.register(Navios, navio_display)
