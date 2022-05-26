from django.db import models
from conteudo.models import Conteudo

class Recursos(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    link = models.CharField(max_length=250)
    id_conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo