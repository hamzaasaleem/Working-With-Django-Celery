import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from enumchoicefield import EnumChoiceField
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from .enums import TimeInterval, SetupStatus


# Create your models here.


class EmailSchedule(models.Model):
    title = models.CharField(max_length=70, blank=False, unique=True)
    email = models.EmailField(unique=True)
    status = EnumChoiceField(SetupStatus, default=SetupStatus.active)

    time_interval_test = models.IntegerField(help_text="Please enter time in minutes", default=5)
    task = models.OneToOneField(
        PeriodicTask,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.email

    def setup_task(self, interval):
        self.task = PeriodicTask.objects.create(
            name=self.title,
            task='computation_heavy_task',
            interval=interval,
            args=json.dumps([self.id]),
            start_time=timezone.now()
        )
        self.save()

    def create_interval(self):
        schedule = IntervalSchedule.objects.create(every=self.time_interval_test, period='minutes')
        return schedule

    def delete(self, *args, **kwargs):
        if self.task is not None:
            self.task.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


@receiver(post_save, sender=EmailSchedule)
def create_or_update_periodic_task(sender, instance, created, **kwargs):
    if created:
        interval = instance.create_interval()
        instance.setup_task(interval)
    else:
        if instance.task is not None:
            instance.status = SetupStatus.active
            interval = instance.task.interval
            interval_schedule = IntervalSchedule.objects.get(id=interval.id)
            interval_schedule.every = instance.time_interval_test
            interval_schedule.save()
            instance.task.enabled = True
            instance.task.save()
