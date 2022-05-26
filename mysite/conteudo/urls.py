from django.urls import path
from . import views

urlpatterns = [
    #urls para a listagem de todos os crusos
    path('', views.listar, name="listar"),
    #url para detalhes de 1 curso
    path('<int:id_conteudo>/', views.detalhar, name="detalhar"),
    path('excluir/<int:id_conteudo>/', views.excluir, name="excluir"),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id_conteudo>/', views.editar, name='editar'),
]