from django.db import models

from datetime import date

class Livro(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False)
    editora = models.CharField(verbose_name="Editora", max_length=15, null=False, blank=False)
    ano = models.DateField(verbose_name="Ano", null=True)