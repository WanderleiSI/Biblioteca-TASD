from django.db import models
from datetime import date
from cliente.models import Cliente
from livro.models import Livro
# Create your models here.


class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, verbose_name="Cpf cliente", on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, verbose_name="Livro", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data inicial", null=False, blank=False)
    finished = models.DateField(verbose_name="Data final", null=True)
    # finished = models.DateTimeField(verbose_name="Data final",null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished:
            self.finished = date.today()
            self.save()
