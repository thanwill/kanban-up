from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from forms.forms import TaskForm
from .models import Task, Comment


# Create your views here.
@login_required
def index(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'users': users,
        'form': form
    }
    return render(request, 'tasks/list.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.all()
    users = User.objects.all()
    status_list = Task.objects.values_list('status', flat=True).distinct()
    selected_status = request.GET.get('status', '')

    if selected_status:
        tasks = tasks.filter(status=selected_status)

    form = TaskForm()
    context = {
        'tasks': tasks,
        'users': users,
        'form': form,
        'status_list': status_list,
        'selected_status': selected_status
    }
    return render(request, 'tasks/list.html', context)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = Comment.objects.filter(task=task)
    comment = comments.first() if comments else None  # Se não houver comentários, comment será None

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')  # Certifique-se de que o redirecionamento está correto
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
        'comment': comment
    }
    return render(request, 'tasks/edit.html', context)


@login_required()
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks:index')


@login_required()
# alterar o usuário da tarefa
def change_user(request, task_id, user_id):
    task = get_object_or_404(Task, pk=task_id)
    user = get_object_or_404(User, pk=user_id)
    task.user = user
    task.save()
    return redirect('tasks:index')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
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


@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    comment = request.POST.get('comment')
    task.comment_set.create(comment=comment, user=request.user)
    return redirect('tasks:edit_task', task_id=task_id)
