from django.urls import path
from . import views
from .views import my_post_view

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('api/post/', my_post_view),
]