from django.urls import path
from . import views  # Importa as views do seu aplicativo

urlpatterns = [
    path('', views.home, name='home'),  # Mapeia a URL raiz para a view 'home'
    # Adicione mais URLs aqui conforme necessário
]
