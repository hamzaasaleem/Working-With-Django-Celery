# Generated by Django 3.2.16 on 2022-12-22 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_emailschedule_time_interval_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailschedule',
            name='time_interval',
        ),
    ]
