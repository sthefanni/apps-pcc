from django.db import models

class Cursos(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    tempo_duracao = models.FloatField()

    def __str__(self):
        return self.titulo