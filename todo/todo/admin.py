from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("text", "is_done", "user", "created", "updated")
    list_filter = ("is_done", "user")
    search_fields = ("text",)
