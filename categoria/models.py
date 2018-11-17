from django.db import models


class Categoria(models.Model):
    descricao = models.CharField('Descrição', max_length=200)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['descricao']
