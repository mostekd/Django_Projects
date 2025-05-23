from django.shortcuts import render, redirect
from .models import Todo, Article
from .forms import TodoForm, PublicTodoForm, ArticleUrlForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserWithArticlesSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .tasks import fetch_article_title

# Widoki HTML
def index(request):
    form = PublicTodoForm()
    if request.method == 'POST':
        form = PublicTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = None
            todo.deadline = None
            todo.public = True
            todo.save()
            return redirect('index')
    todos = Todo.objects.filter(public=True)
    return render(request, 'index.html', {'form': form, 'todos': todos})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form, 'todo': todo})

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'delete.html', {'todo': todo})

@api_view(['POST'])
def my_post_view(request):
    data = request.data
    return Response({"received_data": data})

# API: Wszystkie artykuły
class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# API: Użytkownik + jego artykuły po e-mailu
class UserByEmailAPIView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'detail': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
            serializer = UserWithArticlesSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

def articles_html(request):
    articles = Article.objects.select_related('author').order_by('-created_at')
    return render(request, 'articles.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(title=title, content=content, author=request.user)
            return redirect('articles-html')
        else:
            error = 'Podaj tytuł i treść.'
            return render(request, 'create_article.html', {'error': error})
    return render(request, 'create_article.html')

@login_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id, author=request.user)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles-html')
    return render(request, 'edit_article.html', {'article': article})

@login_required
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id, author=request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('articles-html')
    return render(request, 'delete_article.html', {'article': article})

@login_required
def my_todos(request):
    todos_qs = request.user.todos.all().order_by('deadline')

    # filtrowanie po deadline — np. ?today=true
    if request.GET.get('today') == 'true':
        today = timezone.now().date()
        todos_qs = todos_qs.filter(deadline__date=today)

    paginator = Paginator(todos_qs, 5)  # 5 na stronę
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('my-todos')
    return render(request, 'my_todos.html', {
        'form': form,
        'page_obj': page_obj,
        'today_filter': request.GET.get('today') == 'true'
    })

@login_required
def edit_my_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('my-todos')
    return render(request, 'edit_my_todo.html', {'form': form, 'todo': todo})


@login_required
def delete_my_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('my-todos')
    return render(request, 'delete_my_todo.html', {'todo': todo})

@login_required
def create_article_from_url(request):
    form = ArticleUrlForm()
    error = None
    if request.method == 'POST':
        form = ArticleUrlForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.status = 'none'
            article.save()
            fetch_article_title.delay(article.id)
            return redirect('articles-html')
        else:
            error = 'Podaj poprawny URL.'
    return render(request, 'article_from_url.html', {'form': form, 'error': error})