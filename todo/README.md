# ✅ Django To-Do App — Wersja Rozszerzona

Kompletna aplikacja To-Do w Django dla początkujących programistów, z pełną obsługą użytkowników, zadań, filtrowania, edycji, sortowania, deadline'ów i przypomnień e-mail.

---

## 🧰 Funkcje

- Rejestracja i logowanie użytkowników
- Dodawanie, edycja, usuwanie zadań
- Oznaczanie zadań jako ukończone
- Filtrowanie po statusie (ukończone, nieukończone)
- Wyszukiwanie zadań po tytule
- Sortowanie po dacie deadline'u
- Deadline zadań (data + godzina)
- Przypomnienia e-mail o zbliżających się deadline’ach (komenda `remind_tasks`)

---

## 🧱 Technologie

- Python 3.x
- Django 4.x
- SQLite (domyślna baza danych Django)
- HTML, CSS
- System szablonów Django

---

## 🗃 Struktura Katalogów

```
todo_project/
├── manage.py
├── todo_project/
│   └── settings.py
│   └── urls.py
├── todo/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── todo/
│   │   │   ├── base.html
│   │   │   ├── task_form.html
│   │   │   ├── task_list.html
│   │   │   └── register.html
│   │   └── registration/
│   │       └── login.html
│   ├── static/todo/styles.css
│   └── management/commands/remind_tasks.py
```

---

## ⚙️ Uruchomienie projektu lokalnie

```bash
git clone <repo-url>
cd todo_project
python -m venv venv
source venv/bin/activate  # lub venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📥 Skonfiguruj przypomnienia e-mail

1. W `settings.py` dodaj:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'twojemail@gmail.com'
EMAIL_HOST_PASSWORD = 'haslotoken'
```

2. Uruchom przypomnienie:
```bash
python manage.py remind_tasks
```

3. Możesz dodać do `cron`:
```bash
*/15 * * * * /sciezka/do/venv/bin/python /sciezka/do/manage.py remind_tasks
```

---

## 📊 Model danych: `Task`

| Pole       | Typ              | Opis                             |
|------------|------------------|----------------------------------|
| user       | ForeignKey(User) | Właściciel zadania               |
| title      | CharField        | Tytuł                            |
| description| TextField        | Opis                             |
| complete   | BooleanField     | Czy ukończone?                   |
| deadline   | DateTimeField    | Termin wykonania (opcjonalny)    |
| created    | DateTimeField    | Data utworzenia zadania          |

---

## 🧠 Widoki

- `task_list` – pokazuje zadania, filtruje, sortuje, wyszukuje
- `task_create` – tworzenie zadania
- `task_edit` – edycja istniejącego zadania
- `task_delete` – usuwa zadanie
- `task_toggle` – zmienia status ukończenia
- `register` – rejestracja użytkownika
- `remind_tasks` – komenda do wysyłania przypomnień

---

## 🖥 Szablony

- `base.html` – szablon bazowy dla wszystkich widoków
- `task_list.html` – lista zadań z filtrami, sortowaniem i linkami akcji
- `task_form.html` – formularz dodawania i edycji
- `register.html` – formularz rejestracyjny
- `login.html` – formularz logowania

---

## 🎨 Styl

- Responsywność i nowoczesny wygląd
- Animacje CSS (fadeIn, hover)
- Kolorowanie statusu zadania

---

## 🔐 Bezpieczeństwo

- Widoki zabezpieczone @login_required
- Użytkownik widzi tylko własne zadania
- Adres e-mail potrzebny do przypomnień

---

## 🔔 Przypomnienia e-mail

- Komenda: `python manage.py remind_tasks`
- Wybiera zadania, których deadline nadchodzi w ciągu godziny
- Wysyła przypomnienie na adres użytkownika

---

## 📌 Możliwości rozbudowy

- Kategoryzacja zadań (tagi)
- Powiadomienia push/web
- Dodanie REST API + React frontend
- Automatyczne oznaczanie przeterminowanych zadań

---

Zaprojektowano z myślą o nauce Django — idealny projekt na portfolio! 🚀
