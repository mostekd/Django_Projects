# Django CRUD App z systemem rejestracji, logowania i zarzadzania artykulami

## 📌 Opis projektu

Aplikacja webowa stworzona w Django, umożliwiająca:

* zarządzanie zadaniami (ToDo)
* rejestrację i logowanie użytkowników
* dodawanie, edytowanie i usuwanie artykułów
* przeglądanie wszystkich artykułów oraz artykułów konkretnego użytkownika (także przez API)
* osobisty panel ToDo z przypomnieniami mailowymi
* dodawanie artykułów przez URL do Wikipedii z automatycznym pobieraniem tytułu przez Celery + Redis

## 📁 Struktura folderów

```
crud/
├── manage.py
├── crud/
│   ├── __init__.py
│   ├── celery.py
│   └── settings.py, urls.py, wsgi.py, asgi.py
├── crudapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── tasks.py
│   ├── serializers.py
│   ├── admin.py
│   ├── templates/
│   │   ├── base.html, index.html, register.html, login.html
│   │   ├── articles.html, create_article.html, edit_article.html, delete_article.html,
│   │   ├── article_from_url.html
│   │   ├── my_todos.html, edit_my_todo.html, delete_my_todo.html
│   ├── static/css/style.css
```

## 🚀 Instalacja i uruchomienie

1. Stwórz środowisko:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Zainicjuj bazę danych:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Uruchom Redis i Celery:

```bash
sudo apt install redis-server
redis-server
celery -A crud worker --loglevel=info
```

4. Uruchom serwer Django:

```bash
python manage.py runserver
```

## 👤 Funkcjonalności użytkownika

* Rejestracja konta
* Logowanie i wylogowywanie
* Formularze z walidacją i stylizacją
* Dodawanie artykułów z linka do Wikipedii
* Przycisk „Moje ToDo” i prywatne zadania

## 📝 Panel ToDo (dla zalogowanych)

* Lista zadań: `/my-todos/`
* Kategorie: praca, dom, nauka
* Status: ukończone / nieukończone
* Deadline + przypomnienia e-mailowe (Celery)
* Załączniki do zadań
* Edycja, usuwanie i filtrowanie
* Paginacja i filtr deadline (dzisiaj)

## 🌐 Artykuły z Wikipedii (asynchronicznie)

* Formularz: wpisz URL → tworzony Article (status: `none`)
* Celery odpala task:

  * ustawia `in_progress`
  * pobiera HTML + tag `og:title`
  * ustawia tytuł i `success`
* Wyświetlanie statusu na liście: `⏳`, `✅`, `❌`

## 🔐 Bezpieczeństwo

* Tylko zalogowany użytkownik ma dostęp do prywatnych zasobów
* ToDo dodane z index.html są publiczne, anonimowe i bez deadline

## 🔗 API endpointy (DRF)

* `GET /api/articles/` — wszystkie artykuły
* `GET /api/user-by-email/?email=example@site.com` — artykuły konkretnego użytkownika lub 404

## 🛠️ Panel administracyjny

Dostępny pod `/admin/`:

* Modele: `Article`, `Todo`
* Wyszukiwanie, filtrowanie, sortowanie

## 📦 requirements.txt (fragmenty)

```
django
celery
redis
beautifulsoup4
requests
django-rest-framework
```

## 🎨 Styl

* Stylizacja inputów: tekst, data, checkbox, file
* Formy wyśrodkowane i przejrzyste
* Responsywne przyciski i odstępy

## ✅ Gotowe!

Projekt wspiera interaktywne tworzenie treści + async backend przez Celery + Redis. Wszystko gotowe do rozwoju lub wdrożenia!
