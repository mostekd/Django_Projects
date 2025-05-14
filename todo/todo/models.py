from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "todo"

    def __str__(self):
        return self.text
