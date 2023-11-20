# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotifSerializer, NotifEditSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .permissions import IsNotiOwner
from .filters import NotificationFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class NotificationPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class NotifListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotificationFilter
    pagination_class = NotificationPagination
    serializer_class = NotifSerializer
    permission_classes = [IsNotiOwner]

    def get_queryset(self):
        queryset = Notification.objects.all()

        # Filtering by status

        # Sorting by multiple parameters (name and age)
        ordering_params = self.request.query_params.getlist('sort')

        if ordering_params:
            # If ordering parameters are provided, use them for sorting
            queryset = queryset.order_by(*ordering_params, 'created_at')
        else:
            # If no ordering parameters are provided, do not apply any sorting
            #queryset = queryset.order_by()
            queryset = queryset.order_by('-created_at')

        return queryset


class NotifCreateView(generics.ListCreateAPIView):

    serializer_class = NotifSerializer
    #permission_classes = [IsNotiOwner]

    def get_queryset(self):
        # Filter comments based on the specific shelter or pet seeker
        read = False
        if self.kwargs['status'] == 'read':
            read = True
        queryset = Notification.objects.filter(user=self.request.user, read=read)
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

class NotificationUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = NotifEditSerializer
        permission_classes = [IsNotiOwner]

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
