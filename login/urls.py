from django.urls import path
from .views import index  # Certifique-se de que está importando a view correta

urlpatterns = [
    path('', index, name='login'),  # A URL deve ser uma string vazia para corresponder a 'login/'
]
