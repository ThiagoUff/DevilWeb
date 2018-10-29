from django.db import models


class Imagem(models.Model):
    imagem_desc = models.CharField(max_length=200)
    imagem_src = models.CharField(max_length=200)
    index = models.IntegerField()
    noticia = models.IntegerField()

    def __str__(self):
       return self.imagem_desc

