from multiprocessing import context
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.db import models
from conteudo.forms import ConteudoForm

from conteudo.models import Conteudo

#view de listagem de cursos
def listar(request):
    #recupero todos os cursos que estão na base de dados
    conteudo = Conteudo.objects.all()

    #defino quais as variáveis irão ser passadas pelo contexto
    context = {
        'conteudo': conteudo,
    }
    #renderizando o template para o usuário e passando as variáveis do contexto.
    return render(request, 'conteudo/listar.html', context)

#view de detalhamento de curso
def detalhar(request, id_conteudo):
    conteudo = Conteudo.objects.get(pk = id_conteudo)
    return render(request, 'conteudo/detalhar.html', {'conteudo': conteudo})

#view de exclusão de cucursorso
def excluir(request, id_conteudo):
    Conteudo.objects.get(pk=id_conteudo).delete()
    return HttpResponseRedirect("/conteudo")

#view de criação de  - form não aparece
def criar(request):
    
    if request.method == "POST":
        form = ConteudoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/conteudo")
    else:
        form = ConteudoForm()
    
    context = {
        'form': form
    }
    return render(request,'conteudo/criar.html', context)

#view de edição de usuário
def editar(request, id_conteudo):
    
    conteudo = Conteudo.objects.get(pk=id_conteudo)
    
    if request.method == "POST":
        form = ConteudoForm(request.POST, instance=conteudo)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/conteudo")
    else:
        form = ConteudoForm(instance=conteudo)
    
    context = {
        'form': form,
        'id_conteudo': id_conteudo
    }
    
    
    return render(request, 'conteudo/editar.html', context)





