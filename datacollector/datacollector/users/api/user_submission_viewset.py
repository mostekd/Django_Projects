from rest_framework import viewsets, filters
from datacollector.users.models import UserSubmission
from datacollector.users.serializers import UserSubmissionSerializer

class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'email', 'city', 'birthdate']
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
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
