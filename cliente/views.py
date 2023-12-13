from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Cliente


class ClienteListView(ListView):
    model = Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["nome", "cpf", "email"]
    success_url = reverse_lazy("cliente_list")
    # success_url  = reverse_lazy("todo_create")


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields =  ["nome", "cpf", "email"]
    success_url = reverse_lazy("cliente_list")


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente_list")


class ClienteCompleteView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.mark_has_complete()
        return redirect("cliente_list")
