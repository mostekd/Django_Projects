from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Article

@shared_task
def fetch_article_title(article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'in_progress'
    article.save()

    try:
        response = requests.get(article.url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta = soup.find('meta', property='og:title')
        title = meta['content'] if meta else 'Brak tytułu'
        article.title = title
        article.status = 'success'
    except Exception as e:
        article.title = f'Błąd: {str(e)}'
        article.status = 'error'
    article.save()
