from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todos/todo_form.html"
    fields = ["title", "description", "due_date"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todos/todo_form.html"
    fields = ["title", "description", "due_date"]
    success_url = reverse_lazy("todo_list")


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todos/todo_detail.html"
    context_object_name = "todo"


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todos/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_list")


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")
