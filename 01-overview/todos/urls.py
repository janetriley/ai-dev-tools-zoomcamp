from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo_edit'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]
