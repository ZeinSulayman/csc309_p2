from django.urls import path
from .views import PetListView, PetRetrieveUpdateDestroyView, PetCreateView

urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/create/', PetCreateView.as_view(), name='pet-create'),
    path('pets/<int:pk>/', PetRetrieveUpdateDestroyView.as_view(), name='pet-retrieve-update-destroy'),
]
