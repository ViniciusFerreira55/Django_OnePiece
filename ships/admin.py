from django.contrib import admin
from .models import Characters
# Register your models here.

class characters_display(admin.ModelAdmin):
    list_display = ('id', 'nome_personagem', 'recompensa_personagem', 'tripulacao_personagem', 'akumaNoMi_personagem', 'descricao_personagem', 'foto')
admin.site.register(Characters, characters_display)
