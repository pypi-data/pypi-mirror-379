from rest_framework.generics import ListAPIView, CreateAPIView
from django_msteams_notify.models import TeamsNotification
from django_msteams_notify.serializers import TeamsNotificationSerializer

class TeamsNotificationListAPIView(ListAPIView):
    queryset = TeamsNotification.objects.all().order_by('-sent_at')
    serializer_class = TeamsNotificationSerializer

class TeamsNotificationCreateAPIView(CreateAPIView):
    serializer_class = TeamsNotificationSerializer
    
    def perform_create(self, serializer):
        serializer.save()
