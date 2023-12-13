from django.contrib import admin
from django.urls import path

from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

from cliente.views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    ClienteCompleteView,
)

from livro.views import (
    LivroListView,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
    LivroCompleteView,
)

urlpatterns = [
    #EMPRESTIMO
    path("admin/", admin.site.urls),
    path("principal_todo", TodoListView.as_view(), name="todo_list"),
    path("create_todo", TodoCreateView.as_view(), name="todo_create"),
    path("update_todo/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete_todo/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete_todo/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    #CLIENTE
    path("principal__cliente", ClienteListView.as_view(), name="cliente_list"),
    path("create_cliente", ClienteCreateView.as_view(), name="cliente_create"),
    path("update_cliente/<int:pk>", ClienteUpdateView.as_view(), name="cliente_update"),
    path("delete_cliente/<int:pk>", ClienteDeleteView.as_view(), name="cliente_delete"),
    path("complete_cliente/<int:pk>", ClienteCompleteView.as_view(), name="cliente_complete"),
    #LIVRO
    path("principal__livro", LivroListView.as_view(), name="livro_list"),
    path("create_livro", LivroCreateView.as_view(), name="livro_create"),
    path("update_livro/<int:pk>", LivroUpdateView.as_view(), name="livro_update"),
    path("delete_livro/<int:pk>", LivroDeleteView.as_view(), name="livro_delete"),
    path("complete_livro/<int:pk>", LivroCompleteView.as_view(), name="livro_complete"),
    
]
