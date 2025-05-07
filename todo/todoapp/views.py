from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone

@login_required
def task_list(request):
    search = request.GET.get('search', '')
    filter_by = request.GET.get('filter', 'all')
    sort = request.GET.get('sort', 'asc')

    tasks = Task.objects.filter(user=request.user)

    if search:
        tasks = tasks.filter(title__icontains=search)
    if filter_by == 'done':
        tasks = tasks.filter(complete=True)
    elif filter_by == 'not_done':
        tasks = tasks.filter(complete=False)

    if sort == 'desc':
        tasks = tasks.order_by('-deadline')
    else:
        tasks = tasks.order_by('deadline')

    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'search': search,
        'filter': filter_by,
        'sort': sort,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form, 'edit': False})

@login_required
def task_edit(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form, 'edit': True})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def task_toggle(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('task_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'todo/register.html', {'form': form})