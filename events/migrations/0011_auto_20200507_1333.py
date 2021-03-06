# Generated by Django 3.0.6 on 2020-05-07 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200506_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventTime',
            new_name='endTime',
        ),
        migrations.AddField(
            model_name='event',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
