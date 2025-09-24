from rest_framework.generics import ListAPIView, CreateAPIView
from django_msteams_notify.models import TeamsNotification
from django_msteams_notify.serializers import TeamsNotificationSerializer
from django_msteams_notify.notify import send_notification


class TeamsNotificationListAPIView(ListAPIView):
    queryset = TeamsNotification.objects.all().order_by('-sent_at')
    serializer_class = TeamsNotificationSerializer

class TeamsNotificationCreateAPIView(CreateAPIView):
    serializer_class = TeamsNotificationSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        # Ensure notification task runs safely after DB commit
        transaction.on_commit(lambda: send_notification(instance))