from django.db import models

class AkumaNoMi(models.Model):
    nome_akuma = models.CharField(max_length=50)
    tipo_akuma = models.CharField(max_length=50)
    descricao_akuma = models.TextField()
    foto_akuma = models.ImageField()
    def __str__(self):
        return self.nome_personagem


class Characters(models.Model):
    nome_personagem = models.CharField(max_length=50)
    recompensa_personagem = models.CharField(max_length=50)
    tripulacao_personagem = models.CharField(max_length=50)
    akumaNoMi_personagem = models.CharField(max_length=50)
    descricao_personagem = models.TextField()
    foto = models.ImageField()
    def __str__(self):
        return self.nome_personagem
    

