from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if request.user.is_authenticated:
                task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'pages/home.html', {'form': form, 'tasks': tasks})


@require_POST
@login_required
def finish_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_done = True
    task.save()
    return redirect('home')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'pages/edit_task.html', {'form': form, 'task': task})


@require_POST
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('home')
