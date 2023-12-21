from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail

from todos.models import Todo

class EnvEmailView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        try:
            send_mail('Emprestimo de livro',
                    'E-mail gerado automaticamente pelo sistema\nDevolução de livro atrasada\n', 
                    'bibliotecatasd@gmail.com',
                    [todo.cliente.email],)
            todo.notified = True
            todo.save()
        finally:
            return redirect("todo_list")