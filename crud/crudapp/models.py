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

    def __str__(self):
        return f"{self.name} ({self.user.username})" if self.user else self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    def __str__(self):
        return self.title
