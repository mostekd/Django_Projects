from django.urls import path, include
from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from rest_framework.routers import DefaultRouter
from .views import UserSubmissionViewSet, CityViewSet

router = DefaultRouter()
router.register(r'submissions', UserSubmissionViewSet, basename='submissions')
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('api/', include(router.urls)),
]

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
