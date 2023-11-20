# urls.py

from django.urls import path
from .views import ShelterCommentListCreateView, AppCommentListCreateView

urlpatterns = [
    path('shelters/<int:shelter_id>/comments/', ShelterCommentListCreateView.as_view(), name='shelter-comments'),
    path('apps/<int:application_id>/comments/', AppCommentListCreateView.as_view(), name='app-comments'),
]
