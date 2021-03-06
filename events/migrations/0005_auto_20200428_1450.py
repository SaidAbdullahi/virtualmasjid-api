# Generated by Django 3.0.4 on 2020-04-28 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200428_1325'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='event',
            name='events_even_venue_i_23b7d3_idx',
        ),
        migrations.RemoveIndex(
            model_name='event',
            name='events_even_venue_i_365e6f_idx',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='endDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='frequency',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Daily'), (7, 'Weekly'), (14, 'Biweekly'), (28, 'Monthly')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='stream_medium',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['venue', 'startDate'], name='events_even_venue_i_a66338_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['venue', 'endDate'], name='events_even_venue_i_4e58c8_idx'),
        ),
    ]
