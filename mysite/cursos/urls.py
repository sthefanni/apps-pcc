from django.urls import path
from . import views

urlpatterns = [
    #urls para a listagem de todos os crusos
    path('', views.listar, name="listar"),
    #url para detalhes de 1 curso
    path('<int:id_curso>/', views.detalhar, name="detalhar"),
]