# Generated by Django 4.0.6 on 2022-07-15 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_remove_flight_destination_remove_flight_duration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Flight',
        ),
    ]