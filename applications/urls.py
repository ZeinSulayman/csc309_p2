from django.urls import path
from .views import PetApplicationView, PetApplicationDetailView, PetApplicationUpdateView, ShelterApplicationsListView

urlpatterns = [
    path('pet/<int:pet_id>/application/', PetApplicationView.as_view(), name='api_pet_adoption_application'),
    path('application/<int:application_id>/', PetApplicationDetailView.as_view(), name='adoption_application_detail'),
    path('application/<int:application_id>/status/', PetApplicationUpdateView.as_view(), name='adoption_application_update'),
    path('shelter/applications/', ShelterApplicationsListView.as_view(), name='shelter_applications_list'),
]
