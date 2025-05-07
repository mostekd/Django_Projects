import pytest
from django.urls import reverse
from crudapp.models import Todo

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
