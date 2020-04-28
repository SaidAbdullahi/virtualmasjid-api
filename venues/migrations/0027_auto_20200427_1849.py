# Generated by Django 3.0.4 on 2020-04-27 18:49

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0026_auto_20200112_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='Africa/Nairobi'),
        ),
    ]