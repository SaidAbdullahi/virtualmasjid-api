from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from . import models
from . import serializers
from . import filters
from events.tasks import create_new_events
from datetime import datetime, timedelta


class EventViewSet(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.select_related('venue').order_by(
        'startDate', 'eventTime','venue__name',)
    filterset_class = filters.EventFilterSet
    send_date = datetime.utcnow() + timedelta(hours=24)
    create_new_events.apply_async(eta=send_date)

class CachedListMixin():
    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)