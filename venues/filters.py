from django_filters.rest_framework import (
    FilterSet, OrderingFilter,
)

from . import models

DEFAULT_NUMERIC_FILTER_OPERATORS = [
    'exact', 'lte', 'gte', 'lt', 'gt', 'isnull', 'in',
]

DEFAULT_STRING_FILTER_OPERATORS = [
    'iexact', 'icontains', 'istartswith', 'iendswith', 'startswith',
    'endswith', 'contains', 'exact', 'regex', 'iregex', 'isnull', 'in',
]


class VenueFilterSet(FilterSet):

    o = OrderingFilter(
        fields=[
            'name', 'city', 'events__title'
            'events__speaker', 'events__language',
        ],
    )

    class Meta:
        fields = {
            'name': DEFAULT_STRING_FILTER_OPERATORS,
            'city': DEFAULT_STRING_FILTER_OPERATORS,
            'events__title': DEFAULT_STRING_FILTER_OPERATORS,
            'events__speaker': DEFAULT_STRING_FILTER_OPERATORS,
            'events__language': DEFAULT_STRING_FILTER_OPERATORS,
        }
        model = models.Venue
