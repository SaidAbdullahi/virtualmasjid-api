from django.db import models


class Event(models.Model):
    venue = models.ForeignKey(
        'venues.Venue', models.CASCADE, related_name='events',
    )

    RECURRENCE_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (7, 'Weekly'),
        (14, 'Biweekly'),
        (28, 'Monthly')
    )
    frequency = models.IntegerField(choices=RECURRENCE_CHOICES)
    eventTime = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    title = models.CharField(max_length=50, db_index=True)
    language = models.CharField(max_length=50, blank=True)
    speaker = models.CharField(max_length=50, blank=True)
    stream_medium = models.CharField(max_length=50, blank=True)
    stream_link = models.URLField(blank=True, null=True, unique=True)
    qa_allowed = models.BooleanField(default=False)
    is_live = models.BooleanField(default=True)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=['venue', 'startDate']),
    #         models.Index(fields=['venue', 'endDate']),
    #     ]
    def __str__(self):
        return self.title
