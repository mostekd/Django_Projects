@pytest.mark.django_db
def test_get_articles_api(client):
    response = client.get('/api/articles/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_user_by_email_api(client, django_user_model):
    user = django_user_model.objects.create_user(username='u', email='x@x.com', password='123')
    response = client.get('/api/user-by-email/', {'email': 'x@x.com'})
    assert response.status_code == 200
    assert response.json()['email'] == 'x@x.com'
