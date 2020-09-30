from django_filters import rest_framework as filters
from .models import Room
from django.db.models import Count, Q, F, PositiveIntegerField


class RoomsFilter(filters.FilterSet):

    has_free_space = filters.DateFilter(method='has_free_space_filter')

    def has_free_space_filter(self, queryset, name, value):
        queryset = queryset.annotate(
            free_space=F('capacity')-Count(expression='workerinroom__pk',
                                           filter=Q(
                                               workerinroom__date_of_ending__gte=value,
                                               workerinroom__date_of_beginning__lte=value
                                           ),
                                           output_field=PositiveIntegerField()
                                           )
        ).filter(free_space__gt=0)
        return queryset

    class Meta:
        model = Room
        fields = ('has_free_space', )
