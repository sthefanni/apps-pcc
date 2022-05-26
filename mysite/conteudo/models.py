from django.db import models
from cursos.models import Cursos

class Conteudo(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    link = models.CharField(max_length=250)
    nota_minima = models.FloatField()
    id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo