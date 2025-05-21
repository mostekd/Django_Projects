from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from datacollector.users.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import UserSubmission, Voivodeship, City
from .serializers import UserSubmissionSerializer, CitySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.select_related("voivodeship").all()
    serializer_class = CitySerializer


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None=None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class UserSubmissionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSubmissionSerializer
    pagination_class = UserSubmissionPagination

    def get_queryset(self):
        queryset = UserSubmission.objects.all()
        name = self.request.query_params.get('name')
        city = self.request.query_params.get('city')
        year = self.request.query_params.get('year')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if city:
            queryset = queryset.filter(city__iexact=city)
        if year:
            queryset = queryset.filter(birthdate__year=year)
        return queryset