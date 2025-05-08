# Django CRUD App z systemem rejestracji, logowania i zarzadzania artykulami

## 📌 Opis projektu

Aplikacja webowa stworzona w Django, umożliwiająca:

* zarządzanie zadaniami (ToDo)
* rejestrację i logowanie użytkowników
* dodawanie, edytowanie i usuwanie artykułów
* przeglądanie wszystkich artykułów oraz artykułów konkretnego użytkownika (także przez API)
* osobisty panel ToDo z przypomnieniami mailowymi

## 📁 Struktura folderów

```
crud/
├── manage.py
├── crud/
│   └── settings.py, urls.py, wsgi.py, asgi.py
├── crudapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── serializers.py
│   ├── admin.py
│   ├── templates/
│   │   ├── base.html, index.html, register.html, login.html
│   │   ├── articles.html, create_article.html, edit_article.html, delete_article.html
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

3. Uruchom serwer:

```bash
python manage.py runserver
```

## 👤 Funkcjonalności użytkownika

* Rejestracja konta
* Logowanie i wylogowywanie
* Formularz logowania i rejestracji z walidacją błędów
* Stylowe formularze
* Link powrotu do strony głównej

## 📝 CRUD artykułów (HTML)

Dostępny tylko po zalogowaniu:

* Tworzenie: `/articles/create/`
* Edycja: `/articles/edit/<id>/`
* Usuwanie: `/articles/delete/<id>/`
* Lista: `/articles-html/`

Przyciski "edytuj" i "usuń" pojawiają się tylko przy artykułach autora.

## ✅ Panel ToDo (dla zalogowanych)

* Lista zadań: `/my-todos/`
* Tworzenie zadań z `deadline`
* Edycja i usuwanie tylko własnych zadań
* Stylizowane pola daty
* Przycisk dostępny tylko po zalogowaniu

## ✉️ Przypomnienia mailowe

Zadanie cron lub komenda Django `remind_due_todos`, która:

* sprawdza zadania z deadline < 12h
* wysyła przypomnienia e-mailowe do ich autorów

## 🔐 Bezpieczeństwo

* Tylko zalogowany użytkownik może tworzyć/edytować/susuwać swoje artykuły i zadania
* CSRF włączone, walidacja haseł (min 8 znaków, brak podobieństw do username itd.)

## 🔗 API endpointy (DRF)

* `GET /api/articles/` — zwraca wszystkie artykuły
* `GET /api/user-by-email/?email=example@site.com` — zwraca użytkownika + jego artykuły lub 404

## 🧪 Testy

* `test_views.py` pokrywa podstawowy CRUD ToDo
* Dodatkowe testy API można dodać do `test_api.py`

## 🛠️ Panel administracyjny

Dostępny pod `/admin/`:

* Zarejestrowane modele: `Article`, `Todo`
* W panelu admina można przeglądać, filtrować, edytować i usuwać dane
* Wygodne pola wyszukiwania i sortowania

## 🎨 Styl

* Motyw ciemny + przycisk zmiany trybu (ciemny/jasny)
* Responsywny design
* Spójne przyciski i formularze

## ✅ Gotowe!

Projekt gotowy do użytku, rozszerzania i wdrożenia. Każdy krok został opisany w kodzie i szablonach.

---

Masz pytania lub chcesz rozbudować projekt? Zajrzyj do `views.py`, `forms.py` lub `urls.py`, wszystko jest tam dobrze posegregowane.