from django.db import models
from autor.models import Autor

class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=80)
    autor = models.ManyToManyField(Autor)
    url = models.SlugField('URL', max_length=200, help_text='URL baseada no titulo', unique=True)
    data_publicacao = models.DateField('Data publicação')
    conteudo = models.TextField('Conteudo da página')

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'artigo'
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']