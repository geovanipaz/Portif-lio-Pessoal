from multiprocessing import context
from django.shortcuts import render
from .models import Projeto
# Create your views here.

def projetos_index(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos':projetos
    }
    
    return render(request, 'projetos/projetos_index.html', context)

def projeto_detalhe(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    context = {
        'project':projeto
    }
    return render(request, 'projetos/projeto_detalhe.html', context)
