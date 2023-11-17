from django.urls import path
from .views import NotifCreateView, NotificationUpdateView

urlpatterns = [
    path('noti/<str:status>', NotifCreateView.as_view(), name='noti-create'),
    path('noti/<int:pk>/', NotificationUpdateView.as_view(), name='noti-retrieve-update-destroy'),
]
