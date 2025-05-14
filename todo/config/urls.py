from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("", include("todo.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("todo.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass
    urlpatterns += staticfiles_urlpatterns()
