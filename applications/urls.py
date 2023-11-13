from django.urls import path
from .views import PetApplicationView, PetApplicationDetailView, PetApplicationUpdateView, ShelterApplicationsListView

urlpatterns = [
    path('api/pet/<int:pet_id>/application/', PetApplicationView.as_view(), name='api_pet_adoption_application'),
    path('api/application/<int:application_id>/', PetApplicationDetailView.as_view(), name='adoption_application_detail'),
    path('api/application/<int:appli§cation_id>/update/', PetApplicationUpdateView.as_view(), name='adoption_application_update'),
    path('api/shelter/applications/', ShelterApplicationsListView.as_view(), name='shelter_applications_list'),
]
