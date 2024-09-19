from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = [ 'qualidadedoproduto', 'tempoespera', 'limpeza', 'atendimento', 'buffet', 'cardapio', 'ambiente', 'preco', 'nota', 'comentario', 'anonimo']
