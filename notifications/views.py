# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotifSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect



class NotifCreateView(generics.ListCreateAPIView):
    # Your view logic here for creating a shelter comment
    # ...
    serializer_class = NotifSerializer

    def get_queryset(self):
        # Filter comments based on the specific shelter or pet seeker
        queryset = Notification.objects.filter(user=self.request.user, read=self.kwargs['status'])
        queryset = queryset.order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
    # After creating the comment, create a notification
        serializer.save(user = self.request.user)
    """Notification.objects.create(
        user=shelter_user,
        content=f"A new comment has been added to your shelter: {comment_content}",
        link=shelter_comment_link,
    )
    return Response({"message": "Comment created and notification sent"}, status=status.HTTP_201_CREATED)
"""

class NotificationUpdateView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = NotifSerializer

        def perform_update(self, serializer):
            # Only update the 'read' field
            notif = get_object_or_404(Notification, id=self.kwargs['pk'])
            notif.read=True
            notif.save()

        def get_object(self):
            notif = get_object_or_404(Notification, id=self.kwargs['pk'])
            notif.read=True
            notif.save()
            return notif