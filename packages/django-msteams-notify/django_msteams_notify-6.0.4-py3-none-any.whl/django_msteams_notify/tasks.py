# tasks.py
from celery import shared_task
from django_tenants.utils import schema_context
from django_msteams_notify.models import TeamsNotification
from django_msteams_notify.utils import send_teams_message

@shared_task(bind=True, max_retries=3)
def send_teams_notification_task(self, notification_id, schema_name):
    """
    Send a Teams notification in the context of a tenant schema.
    Retries automatically on failure with exponential backoff.
    """
    try:
        with schema_context(schema_name):
            notification = TeamsNotification.objects.get(id=notification_id)
            # Send message with timeout
            success = send_teams_message(notification, timeout=10)
            notification.status = "sent" if success else "failed"
            notification.save(update_fields=["status"])
            return success
    except TeamsNotification.DoesNotExist:
        print(f"Notification {notification_id} not found in schema {schema_name}")
        return False
    except Exception as exc:
        print(f"Exception in Celery task: {exc}")
        # Retry with exponential backoff
        raise self.retry(exc=exc, countdown=2 ** self.request.retries * 60)
