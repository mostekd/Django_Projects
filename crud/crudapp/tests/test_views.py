import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from crudapp.models import Todo, Article

@pytest.mark.django_db
def test_homepage_get(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_todo(client):
    response = client.post(reverse('index'), {'name': 'Nowe zadanie'})
    assert response.status_code == 302  # przekierowanie po dodaniu
    assert Todo.objects.filter(name='Nowe zadanie').exists()

@pytest.mark.django_db
def test_update_todo(client):
    todo = Todo.objects.create(name="Stare zadanie")
    response = client.post(reverse('update', args=[todo.id]), {'name': 'Zaktualizowane'})
    assert response.status_code == 302
    todo.refresh_from_db()
    assert todo.name == 'Zaktualizowane'

@pytest.mark.django_db
def test_delete_todo(client):
    todo = Todo.objects.create(name="Do usunięcia")
    response = client.post(reverse('delete', args=[todo.id]))
    assert response.status_code == 302
    assert not Todo.objects.filter(id=todo.id).exists()

@pytest.mark.django_db
def test_article_str():
    user = User.objects.create_user(username='testuser', password='123')
    article = Article.objects.create(title='Test Title', content='Test content', author=user)
    assert str(article) == 'Test Title'

@pytest.fixture
def user():
    return User.objects.create_user(username='john', password='pass')

@pytest.fixture
def auth_client(client, user):
    client.force_login(user)
    return client

@pytest.mark.django_db
def test_article_list_api(client):
    response = client.get('/api/articles/')
    assert response.status_code == 200