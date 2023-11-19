from django.urls import path
from .views import NotifCreateView, NotificationUpdateDestroyView, NotifListView

urlpatterns = [
    path('noti/newnoti/<str:status>/', NotifCreateView.as_view(), name='noti-create'),
    path('noti/<int:pk>/', NotificationUpdateDestroyView.as_view(), name='noti-retrieve-update-destroy'),
    path('noti/', NotifListView.as_view(), name='noti-list')
]
