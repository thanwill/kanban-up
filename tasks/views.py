from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from forms.forms import TaskForm
from .models import Task


# Create your views here.
@login_required
def index(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'tasks/index.html', {'tasks': tasks, 'users': users, 'form': form})


@login_required
def get_tasks():
    return Task.objects.all()


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print("Formulário é válido")
            print("Dados do formulário:", form.cleaned_data)
            task = Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                user=form.cleaned_data['user'],
                due_date=form.cleaned_data['due_date'],
            )
            task.save()
            return redirect('tasks:index')
        else:
            print("Formulário não é válido")
            print("Erros do formulário:", form.errors)
    else:
        print("Método de requisição não é POST")
    return redirect('tasks:index')
