from django_filters.rest_framework import (
    FilterSet, OrderingFilter, CharFilter, BooleanFilter,
)
from django.db.models import Q, F

from . import models

DEFAULT_NUMERIC_FILTER_OPERATORS = [
    'exact', 'lte', 'gte', 'lt', 'gt', 'isnull', 'in',
]

DEFAULT_STRING_FILTER_OPERATORS = [
    'iexact', 'icontains', 'istartswith', 'iendswith', 'startswith',
    'endswith', 'contains', 'exact', 'regex', 'iregex', 'isnull', 'in',
]


class EventOrderingFilter(OrderingFilter):

    def get_ordering_value(self, param):
        value = super().get_ordering_value(param)
        return value

class EventFilterSet(FilterSet):

    o = EventOrderingFilter(
        fields=[
            'title', 'speaker', 'language', 'stream_medium',
        ],
    )

    search = CharFilter(method='filter_search')
    on_event = BooleanFilter(method='filter_on_event')

    def filter_search(self, queryset, name, value):
        base_cond = Q()
        # what I want to search for:
        # each word (split by whitespace) is included in at least
        # one of the below six fields,
        # so you can search for "straight monkey" to get monkeynaut
        # or "belgi ipa ommeg" to get all Ommegang Belgian IPAs
        for word in value.split():
            base_cond &= Q(
                title__icontains=word,
            ) | Q(
                speaker__icontains=word,
            ) | Q(
                language__icontains=word,
            ) | Q(
                stream_medium__icontains=word,
            )
        queryset = queryset.filter(base_cond).distinct()
        return queryset

    def filter_on_event(self, queryset, name, value):
        return queryset.filter(title__isnull=not value).distinct()

    class Meta:
        fields = {
            'title': DEFAULT_STRING_FILTER_OPERATORS,
            'speaker': DEFAULT_STRING_FILTER_OPERATORS,
            'language': DEFAULT_STRING_FILTER_OPERATORS,
            'stream_medium': DEFAULT_STRING_FILTER_OPERATORS,
            'venue__name': DEFAULT_STRING_FILTER_OPERATORS,
            'search': ['exact'],
            'on_event': ['exact'],
            'venue__slug': DEFAULT_STRING_FILTER_OPERATORS,
        }
        model = models.Event
