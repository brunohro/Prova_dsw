from django.shortcuts import render
from .models import Modalidade, Equipe, Tecnico, Atleta

def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, "jogos/index.html", {"equipes": equipes, "modalidades": modalidades})

def equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    tecnico = Tecnico.objects.filter(id=id)
    return render(request, "jogos/equipe.html", {"equipe": equipe, "tecnico": tecnico})

def modalidade(request, id):
    modalidade_id = Modalidade.objects.get(id=id)
    return render(request, "jogos/modalidade.html", {"modalidade": modalidade_id})
