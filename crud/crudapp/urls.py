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
]

