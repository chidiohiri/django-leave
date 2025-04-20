import django_filters
from .models import LeaveRequest

class LeaveRequestFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LeaveRequest
        fields = ['title', 'status']