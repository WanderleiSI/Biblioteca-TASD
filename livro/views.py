from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Livro


class LivroListView(ListView):
    model = Livro


class LivroCreateView(CreateView):
    model = Livro
    fields = ["nome", "editora", "ano"]
    success_url = reverse_lazy("livro_list")
    # success_url  = reverse_lazy("todo_create")


class LivroUpdateView(UpdateView):
    model = Livro
    fields =  ["nome", "editora", "ano"]
    success_url = reverse_lazy("livro_list")


class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy("livro_list")


class LivroCompleteView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Livro, pk=pk)
        cliente.mark_has_complete()
        return redirect("livro_list")
