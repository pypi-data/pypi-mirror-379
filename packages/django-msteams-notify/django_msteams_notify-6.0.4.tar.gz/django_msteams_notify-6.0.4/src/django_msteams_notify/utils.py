import requests
from django.conf import settings
from django_msteams_notify.models import TeamsNotification

def send_teams_message(notification: TeamsNotification, timeout=10):
    """
    Send a Teams message via webhook.
    Returns True if sent, False if failed.
    """
    webhook_url = getattr(settings, "TEAMS_WEBHOOK_URL", None)
    if not webhook_url:
        notification.status = "failed"
        notification.save(update_fields=["status"])
        return False

    try:
        response = requests.post(webhook_url, json={"text": notification.message}, timeout=timeout)
        if response.status_code == 200:
            return True
        else:
            print(f"Teams returned status {response.status_code}")
            return False
    except requests.RequestException as exc:
        print(f"Teams message exception: {exc}")
        return False
