import os

import django
from celery import Celery
from . import celeryconfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-celery-demo.settings')
django.setup()

app = Celery('django-celery-demo',
             broker=celeryconfig.CELERY_BROKER_URL,
             backend=celeryconfig.CELERY_BACKEND,
             )

app.config_from_object('django-celery-demo.celeryconfig', namespace='CELERY')

app.autodiscover_tasks()

@app.task()
def add(x, y):
    return x + y



