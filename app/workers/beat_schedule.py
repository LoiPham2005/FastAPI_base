# Celery beat schedule
from .celery_app import celery_app

celery_app.conf.beat_schedule = {
    "cleanup-expired-bookings": {
        "task": "app.features.bookings.tasks.cleanup_expired",
        "schedule": 3600.0,
    },
}
