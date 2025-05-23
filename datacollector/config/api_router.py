from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from datacollector.users.api.views import UserViewSet, UserSubmissionViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("submissions", UserSubmissionViewSet)


app_name = "api"
urlpatterns = router.urls
