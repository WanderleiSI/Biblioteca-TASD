from django.db import models

from datetime import date

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    cpf = models.CharField( verbose_name="cpf", max_length=11, null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=True)


    def __str__(self):
        return self.cpf