"""Models related to Venues"""

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from timezone_field.fields import TimeZoneField
from django_countries.fields import CountryField


class Venue(models.Model):

    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    facebook_page = models.URLField(blank=True)
    twitter_handle = models.CharField(blank=True, max_length=25)
    instagram_handle = models.CharField(blank=True, max_length=25)
    mxlr_handle = models.CharField(blank=True, max_length=25)
    youtube_channel = models.CharField(blank=True, max_length=25)
    spreaker_channel = models.CharField(blank=True, max_length=25)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    logo_url = models.URLField(blank=True)
    slug = models.SlugField()
    # -90 to +90
    latitude = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True,
    )
    # -180 to 180
    longitude = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True,
    )

    def __str__(self):
        return self.name