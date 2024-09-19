from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Certifique-se de que o template existe

from django.shortcuts import render, redirect
from .models import Avaliacao
from .forms import AvaliacaoForm  # Assumindo que você criará um formulário em forms.py

def nova_avaliacao(request):
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial após salvar
    else:
        form = AvaliacaoForm()
    
    return render(request, 'nova_avaliacao.html', {'form': form})
