from django.db import models

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, db_index=True)
    caminho = models.CharField(max_length=200, db_index=True)

    class Meta:
        db_table = 'images'
        ordering = ('id',)

    def __str__(self):
        return self.nome