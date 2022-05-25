from multiprocessing import context
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.db import models
from cursos.forms import CursosForm

from cursos.models import Cursos

#view de listagem de cursos
def listar(request):
    #recupero todos os cursos que estão na base de dados
    cursos = Cursos.objects.all()

    #defino quais as variáveis irão ser passadas pelo contexto
    context = {
        'cursos': cursos,
    }
    #renderizando o template para o usuário e passando as variáveis do contexto.
    return render(request, 'cursos/listar.html', context)

#view de detalhamento de curso
def detalhar(request, id_curso):
    cursos = Cursos.objects.get(pk = id_curso)
    return render(request, 'cursos/detalhar.html', {'cursos': cursos})

#view de exclusão de curso
def excluir(request, id_curso):
    Cursos.objects.get(pk=id_curso).delete()
    return HttpResponseRedirect("/cursos")

#view de criação de curso - form não aparece
def criar(request):
    
    if request.method == "POST":
        form = CursosForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cursos")
    else:
        form = CursosForm()
    
    context = {
        'form': form
    }
    return render(request,'cursos/criar.html', context)

#view de edição de usuário
def editar(request, id_curso):
    
    cursos = Cursos.objects.get(pk=id_curso)
    
    if request.method == "POST":
        form = CursosForm(request.POST, instance=cursos)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cursos")
    else:
        form = CursosForm(instance=cursos)
    
    context = {
        'form': form,
        'id_curso': id_curso
    }
    
    
    return render(request, 'cursos/editar.html', context)





