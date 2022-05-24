from django.urls import path
from .views import TodoAddView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView, todo_add, todo_delete, todo_details, todo_list, todo_update
urlpatterns = [
    # path('', todo_list, name='list'),
    path('', TodoListView.as_view(), name="list"),
    # path('todo-add/', todo_add, name="add"),
    path('todo-add/', TodoAddView.as_view(), name="add"),
    # path('todo-update/<int:pk>', todo_update, name="update"),
    path('todo-update/<int:pk>', TodoUpdateView.as_view(), name="update"),
    # path('todo-details/<int:pk>', todo_details, name="details"),
    path('todo-details/<int:pk>', TodoDetailView.as_view(), name="details"),
    # path('todo-delete/<int:pk>', todo_delete, name="delete"),
    path('todo-delete/<int:pk>', TodoDeleteView.as_view(), name="delete"),
]