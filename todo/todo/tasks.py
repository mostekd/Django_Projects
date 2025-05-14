import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Article

@shared_task
def fetch_wikipedia_article(article_id):
    article = Article.objects.get(id=article_id)
    try:
        response = requests.get(article.url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else article.url
        content = ''
        content_div = soup.find('div', {'id': 'mw-content-text'})
        if content_div:
            paragraphs = content_div.find_all('p', recursive=True)
            content = '\n\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        article.title = title
        article.content = content or '(brak treści)'
        article.status = 'success'
    except Exception as e:
        article.title = 'Błąd'
        article.content = str(e)
        article.status = 'error'
    article.save()
