from django.db import models
from django.shortcuts import render, redirect
#from .models import Avaliacao

# Create your models here.
class Avaliacao(models.Model):
    data = models.DateField(auto_now_add=True)
    qualidadedoproduto = models.IntegerField()
    tempoespera = models.IntegerField()
    limpeza = models.IntegerField()
    atendimento = models.IntegerField()
    buffet = models.IntegerField()
    cardapio = models.IntegerField()
    ambiente = models.IntegerField()
    preco = models.IntegerField()
    nota = models.FloatField()
    comentario = models.TextField()
    anonimo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Avaliação {self.id} - Nota: {self.nota}"