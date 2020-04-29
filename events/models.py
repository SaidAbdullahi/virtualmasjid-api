from django.db import models


class Event(models.Model):
    venue = models.ForeignKey(
        'venues.Venue', models.CASCADE, related_name='events',
    )
    class Recurrence(models.TextChoices):
        ONCE =  "Once"
        DAILY =  "Daily"
        WEEKLY = "Weekly"
        BIWEEKLY = "Biweekly"
        MONTHLY = "Monthly"

    frequency = models.CharField(
        max_length=10,
        choices=Recurrence.choices,
        default=Recurrence.ONCE
    )
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

    def __str__(self):
        return self.title
