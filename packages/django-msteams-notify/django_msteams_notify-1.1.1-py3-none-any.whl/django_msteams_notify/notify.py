from django.db import transaction
from django.db import connection
from django_tenants.utils import schema_exists
from django_msteams_notify.tasks import send_teams_notification_task

def send_notification(instance):
    """
    Enqueue a Teams notification task safely after DB commit.
    Handles multi-tenant and schema validation.
    """
    schema_name = getattr(connection, "schema_name", "public")

    # Validate schema exists
    if not schema_exists(schema_name):
        print(f"Tenant schema {schema_name} does not exist")
        instance.status = "failed"
        instance.save(update_fields=["status"])
        return

    # Enqueue task only after transaction commit
    transaction.on_commit(lambda: send_teams_notification_task.delay(str(instance.id), schema_name))
