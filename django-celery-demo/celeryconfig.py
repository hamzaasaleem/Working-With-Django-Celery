from decouple import config
# Celery settings
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_BACKEND = "redis://127.0.0.1:6379"
