from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name="listar"),
    path('<int:id_recursos>/', views.detalhar, name="detalhar"),
    path('excluir/<int:id_recursos>/', views.excluir, name="excluir"),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id_recursos>/', views.editar, name='editar'),
]