from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Article

@shared_task
def fetch_article_title(article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'in_progress'
    article.save()

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyDjangoApp/1.0; +http://localhost)"
    }

    try:
        response = requests.get(article.url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        meta = soup.find('meta', property='og:title')
        article.title = meta['content'] if meta else 'Brak tytułu'

        content_div = soup.find('div', {'id': 'mw-content-text'})
        paragraphs = content_div.find_all('p', recursive=True) if content_div else []
        text = '\n\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        article.content = text[:3000] if text else '(brak treści)'

        article.status = 'success'
    except Exception as e:
        article.title = 'Błąd'
        article.content = str(e)
        article.status = 'error'

    article.save()
