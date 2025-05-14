from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Task, Article
from .forms import TaskForm, ArticleForm
from django.views.decorators.http import require_POST
from .tasks import fetch_wikipedia_article


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if request.user.is_authenticated:
                task.user = request.user
            else:
                task.user = None
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-created')
    else:
        tasks = Task.objects.filter(user=None).order_by('-created')
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


def articles(request):
    message = None
    if request.method == 'POST' and request.user.is_authenticated:
        if 'wiki_url' in request.POST:
            url = request.POST.get('wiki_url')
            if url:
                article = Article.objects.create(user=request.user, url=url, title='', content='', status='pending')
                fetch_wikipedia_article.delay(article.id)
                return redirect('articles')
            else:
                message = 'Podaj poprawny adres URL.'
        elif 'manual_title' in request.POST and 'manual_content' in request.POST:
            title = request.POST.get('manual_title')
            content = request.POST.get('manual_content')
            if title and content:
                Article.objects.create(user=request.user, title=title, content=content, url='', status='success')
                return redirect('articles')
            else:
                message = 'Podaj tytuł i treść.'
        form = ArticleForm()
    else:
        form = ArticleForm()
    articles = Article.objects.all().order_by('-created')
    return render(request, 'pages/articles.html', {'form': form, 'articles': articles, 'message': message})


@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('manual_title')
        content = request.POST.get('manual_content')
        if title and content:
            article.title = title
            article.content = content
            article.save()
            return redirect('articles')
    return render(request, 'pages/edit_article.html', {'article': article})


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, user=request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'pages/delete_article.html', {'article': article})


def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Artykuł nie istnieje.")
    return render(request, 'pages/article_detail.html', {'article': article})
