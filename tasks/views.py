from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
def task_list(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    done_tasks_count = tasks.filter(status='DONE').count()
    pending_tasks_count = tasks.filter(status='TODO').count()
    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'done_tasks_count': done_tasks_count,
        'pending_tasks_count': pending_tasks_count,
    }
    return render(request, 'tasks/index.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.user = form.cleaned_data['user']
            task.due_date = form.cleaned_data['due_date']
            task.save()
            return redirect('tasks:index')
        else:
            print("Formulário não é válido")
            print("Erros do formulário:", form.errors)
    else:
        form = TaskForm({
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'user': task.user,
            'due_date': task.due_date,
        })
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks:index')


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
