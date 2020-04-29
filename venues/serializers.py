"""Serializers for venues"""


from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from .fields import TimeZoneField
from . import models


class VenueSerializer(CountryFieldMixin, serializers.ModelSerializer):

    time_zone = TimeZoneField(
        required=False, allow_blank=False, allow_null=False,
    )
    latitude = serializers.DecimalField(
        max_digits=10, decimal_places=8, min_value=-90, max_value=90,
        required=False, allow_null=True,
    )
    longitude = serializers.DecimalField(
        max_digits=11, decimal_places=8, min_value=-180, max_value=180,
        required=False, allow_null=True,
    )

    class Meta:
        model = models.Venue
        fields = '__all__'

class VenueBySlugSerializer(VenueSerializer):
    class Meta(VenueSerializer.Meta):
        lookup_field = 'slug'

