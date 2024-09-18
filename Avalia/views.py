from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Certifique-se de que o template existe