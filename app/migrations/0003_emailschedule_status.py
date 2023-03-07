# Generated by Django 3.2.16 on 2022-12-21 19:26

import app.enums
from django.db import migrations
import enumchoicefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_emailschedule_schedule_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailschedule',
            name='status',
            field=enumchoicefield.fields.EnumChoiceField(default=app.enums.SetupStatus['active'], enum_class=app.enums.SetupStatus, max_length=8),
        ),
    ]
