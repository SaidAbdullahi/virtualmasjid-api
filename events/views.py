from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
from . import filters

class EventViewSet(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.select_related('venue').order_by(
        'startDate', 'eventTime','venue__name',
    )
    filterset_class = filters.EventFilterSet
