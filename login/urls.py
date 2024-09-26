from django.urls import path

from .views import index, register  # Certifique-se de que está importando a view correta

urlpatterns = [
    path('', index, name='login'),
    path('register/', register, name='register'),
    path('login/', index, name='login'),
    path('logout/', index, name='logout'),
]
