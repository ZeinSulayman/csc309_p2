from django.urls import path
from .views import PetListCreateView, PetRetrieveUpdateDestroyView

urlpatterns = [
    path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
    path('pets/<int:pk>/', PetRetrieveUpdateDestroyView.as_view(), name='pet-retrieve-update-destroy'),
]
