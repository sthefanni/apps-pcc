from multiprocessing import context
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.db import models
from recursos.forms import RecursosForm

from recursos.models import Recursos

#view de listagem de cursos
def listar(request):
    #recupero todos os cursos que estão na base de dados
    recursos = Recursos.objects.all()

    #defino quais as variáveis irão ser passadas pelo contexto
    context = {
        'recursos': recursos,
    }
    #renderizando o template para o usuário e passando as variáveis do contexto.
    return render(request, 'recursos/listar.html', context)

#view de detalhamento de curso
def detalhar(request, id_recursos):
    recursos = Recursos.objects.get(pk = id_recursos)
    return render(request, 'recursos/detalhar.html', {'recursos': recursos})

#view de exclusão de cucursorso
def excluir(request, id_recursos):
    Recursos.objects.get(pk=id_recursos).delete()
    return HttpResponseRedirect("/recursos")

#view de criação de  - form não aparece
def criar(request):
    
    if request.method == "POST":
        form = RecursosForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/recursos")
    else:
        form = RecursosForm()
    
    context = {
        'form': form
    }
    return render(request,'recursos/criar.html', context)

#view de edição de usuário
def editar(request, id_recursos):
    
    recursos = Recursos.objects.get(pk=id_recursos)
    
    if request.method == "POST":
        form = RecursosForm(request.POST, instance=recursos)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/recursos")
    else:
        form = RecursosForm(instance=recursos)
    
    context = {
        'form': form,
        'id_recursos': id_recursos
    }
    
    return render(request, 'recursos/editar.html', context)



