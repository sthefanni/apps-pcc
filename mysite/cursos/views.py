from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Cursos

#view de listagem de cursos
def listar(request):
    #recupero todos os cursos que estão na base de dados
    cursos = Cursos.objects.all()

    #defino quais as variáveis irão ser passadas pelo contexto
    context = {
        'cursos': cursos
    }
    #renderizando o template para o usuário e passando as variáveis do contexto.
    return render(request, 'cursos/listar.html', context)

#view de detalhamento de curso
def detalhar(request, id_curso):

    return render(request, 'cursos/detalhar.html', {})
    

