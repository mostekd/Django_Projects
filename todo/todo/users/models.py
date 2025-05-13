from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Praca'),
        ('home', 'Dom'),
        ('study', 'Nauka'),
        ('other', 'Inne'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True)
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    public = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} ({self.user.username})" if self.user else self.name


class Article(models.Model):
    class Status(models.TextChoices):
        NONE = 'none', 'Oczekuje'
        IN_PROGRESS = 'in_progress', 'W trakcie pobierania'
        SUCCESS = 'success', 'Gotowe'
        ERROR = 'error', 'Błąd'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NONE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.url