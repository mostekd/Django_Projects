from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('finish/<int:task_id>/', views.finish_task, name='finish_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('articles/', views.articles, name='articles'),
]
