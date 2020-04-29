from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from . import models
from . import filters


class VenueViewSet(ModelViewSet):
    serializer_class = serializers.VenueSerializer
    queryset = models.Venue.objects.order_by('name')
    filterset_class = filters.VenueFilterSet


class VenueBySlugViewSet(VenueViewSet):

    def list(self, request, *args, **kwargs):
        raise NotFound()

    lookup_field = 'slug'
    serializer_class = serializers.VenueBySlugSerializer
