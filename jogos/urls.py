from django.urls import path
from .views import index, equipe, modalidade

urlpatterns = [
    path('', index, name="index"),
    path('equipes/<int:id>', equipe, name="equipe"),
    path('modalidades/<int:id>', modalidade, name="modalidade"),
]
