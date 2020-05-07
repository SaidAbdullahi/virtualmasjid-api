from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from events.views import EventViewSet, CachedListMixin
from events.filters import EventFilterSet
from . import serializers
from . import models
from . import filters


class VenueViewSet(CachedListMixin, ModelViewSet):
    serializer_class = serializers.VenueSerializer
    queryset = models.Venue.objects.order_by('name')
    filterset_class = filters.VenueFilterSet

    @method_decorator(cache_page(60 * 5))
    @action(detail=True, methods=['GET'])
    def events(self, request, pk=None, slug=None):
        filter_cond = {}
        if pk and slug:
            raise serializers.serializers.ValidationError({
                'non_field_errors': [
                    "Somehow you managed to submit both a PK and a slug. "
                    "This isn't possible.",
                ]
            })
        if pk:
            filter_cond['venue__id'] = pk
        elif slug:
            filter_cond['venue__slug'] = slug
        else:
            raise serializers.serializers.ValidationError({
                'non_field_errors': [
                    "Somehow you managed to submit neither a PK nor a slug. "
                    "This isn't possible.",
                ]
            })
        queryset = EventViewSet.queryset.filter(**filter_cond).distinct()

        queryset = EventFilterSet(request.query_params, queryset=queryset).qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EventViewSet.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = EventViewSet.serializer_class(queryset, many=True)
        return Response(serializer.data)


class VenueBySlugViewSet(VenueViewSet):

    def list(self, request, *args, **kwargs):
        raise NotFound()

    lookup_field = 'slug'
    serializer_class = serializers.VenueBySlugSerializer
