from rest_framework import serializers

from venues.models import Venue
from venues.serializers import VenueSerializer
from . import models

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    venue_id = serializers.PrimaryKeyRelatedField(
        write_only=True, required=True, allow_null=False,
        queryset=Venue.objects.all(),
    )

    def validate(self, data):
        try:
            start = data['startDate']
            end = data['endDate']
        except KeyError:
            # must be in a patch; don't care
            pass
        else:
            if start >= end:
                raise serializers.ValidationError({
                    'startDate': [
                        'This must be before endDate',
                    ],
                    'endDate': [
                        'This must be after startDate',
                    ]
                })
        try:
            data['venue'] = data.pop('venue_id')
        except KeyError:
            # must be in a patch; don't care
            pass
        return data

    class Meta:
        model = models.Event
        fields = '__all__'
