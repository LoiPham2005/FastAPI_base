# Celery configuration
from celery import Celery

celery_app = Celery("worker", broker="redis://localhost:6379/0")
celery_app.autodiscover_tasks(["app.features.bookings", "app.features.payments"])
