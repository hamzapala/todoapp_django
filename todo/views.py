from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import TodosForm

from .models import Todos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.

def todo_list(request):
    todos = Todos.objects.all()

    context = {
        "todos": todos
    }
    return render(request, 'todo/todos_list.html', context)

class TodoListView(ListView):
    model = Todos
    context_object_name = 'todos'
    paginate_by: 10


def todo_add(request):
    form= TodosForm()
    if request.method == 'POST':
        form= TodosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form,
    }
    return render(request, 'todo/todos_add.html', context)

class TodoAddView(CreateView):
    model= Todos
    form_class= TodosForm
    template_name= 'todo/todos_add.html' 
    success_url = reverse_lazy("list")




def todo_update(request, id):
    todo= Todos.objects.get(id=id)
    form= TodosForm(instance=todo)
    if request.method == 'POST':
        form= TodosForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form,
    }
    return render(request, 'todo/todos_update.html', context)

class TodoUpdateView(UpdateView):
    model = Todos
    form_class = TodosForm
    template_name = 'todo/todos_update.html'
    success_url= reverse_lazy("list")


def todo_details(request, id):
    todo =Todos.objects.get(id=id)
    return render(request, "todo/todos_detail.html", {"todo":todo})

class TodoDetailView(DetailView):
    model= Todos

def todo_delete(request, id):
    todo =Todos.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect("list")
    return render(request, "todo/todos_delete.html")

class TodoDeleteView(DeleteView):
    model = Todos
    template_name= "todo/todos_delete.html"
    success_url= reverse_lazy("list")