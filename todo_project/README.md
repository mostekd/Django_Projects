# 📝 Django To-Do App

Nowoczesna aplikacja To-Do stworzona w Django, zawierająca rejestrację, logowanie, dodawanie zadań, filtrowanie oraz wyszukiwarkę.

## 🎯 Funkcje
- ✅ Rejestracja i logowanie użytkownika
- 🆕 Dodawanie zadań
- ✔️ Oznaczanie jako ukończone / nieukończone
- ❌ Usuwanie zadań
- 🔍 Filtrowanie i wyszukiwanie zadań

## 🧱 Technologie
- Python 3.x
- Django 4.x
- HTML5 + CSS3
- Wbudowany silnik szablonów Django

## 📦 Instalacja

```bash
git clone <repo-url>
cd todo_project
python -m venv venv
source venv/bin/activate  # lub venv\Scripts\activate na Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Otwórz przeglądarkę i przejdź do: `http://127.0.0.1:8000/`

## 🗃 Model danych

**Task**
| Pole        | Typ               | Opis                         |
|-------------|--------------------|------------------------------|
| user        | ForeignKey (User)  | Właściciel zadania           |
| title       | CharField          | Tytuł zadania                |
| description | TextField          | Szczegóły zadania (opcjonalne) |
| complete    | BooleanField       | Status: ukończone / nie      |
| created     | DateTimeField      | Data utworzenia              |

## 🖥 Widoki

- `/` – lista zadań z wyszukiwarką i filtrem
- `/create/` – formularz tworzenia zadania
- `/toggle/<id>/` – zmiana statusu zadania
- `/delete/<id>/` – usuwanie zadania
- `/register/` – rejestracja użytkownika
- `/login/`, `/logout/` – logowanie i wylogowanie

## 🎨 Styl i UX

- Responsive design (działa dobrze również na telefonach)
- Animacje (hover, fade-in, skalowanie)
- Estetyczny wygląd z nowoczesnymi formularzami i kolorami

## 📁 Struktura katalogów

```
todo_project/
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/todo/
│   ├── static/todo/styles.css
├── templates/registration/login.html
├── manage.py
```

## 🔒 Bezpieczeństwo

- Dostęp do zadań ma tylko zalogowany użytkownik
- Użytkownik widzi wyłącznie swoje zadania

## 📌 Przyszłe rozszerzenia

- 🗓 Deadline i sortowanie po dacie
- 🏷 Kategorie lub tagi zadań
- ✏️ Edycja zadania po utworzeniu

---

Zaprojektowano z myślą o początkujących, którzy chcą zbudować swój pierwszy projekt Django 🚀
