# Generated by Django 3.2.16 on 2022-12-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_emailschedule_time_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailschedule',
            name='title',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
