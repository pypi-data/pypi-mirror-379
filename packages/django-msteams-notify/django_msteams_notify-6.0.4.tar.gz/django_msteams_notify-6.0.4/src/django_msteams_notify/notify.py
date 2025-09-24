from django.db import connection
from django_msteams_notify.tasks import send_teams_notification_task

def send_notification(instance):
    """
    Enqueue Teams notification via Celery.
    Production-safe: no synchronous fallback, retries handled in Celery.
    """
    schema_name = getattr(connection, "schema_name", "public")
    send_teams_notification_task.delay(str(instance.id), schema_name)
