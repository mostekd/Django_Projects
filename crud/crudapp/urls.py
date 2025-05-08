from django.urls import path
from . import views
from .views import my_post_view, ArticleListAPIView, UserByEmailAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('api/post/', my_post_view),
    path('api/articles/', ArticleListAPIView.as_view(), name='articles'),
    path('api/user-by-email/', UserByEmailAPIView.as_view(), name='user-by-email'),
    path('articles-html/', views.articles_html, name='articles-html'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('articles/create/', views.create_article, name='create-article'),
    path('articles/edit/<int:article_id>/', views.edit_article, name='edit-article'),
    path('articles/delete/<int:article_id>/', views.delete_article, name='delete-article'),
    path('my-todos/', views.my_todos, name='my-todos'),
    path('my-todos/edit/<int:todo_id>/', views.edit_my_todo, name='edit-my-todo'),
    path('my-todos/delete/<int:todo_id>/', views.delete_my_todo, name='delete-my-todo'),
]

