from django.contrib import admin
from .models import Task, Article

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("text", "is_done", "user", "created", "updated")
    list_filter = ("is_done", "user")
    search_fields = ("text",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "status")
    search_fields = ("title", "url")
    list_filter = ("status", "user")
