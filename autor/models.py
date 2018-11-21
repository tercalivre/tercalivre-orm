from django.db import models

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

