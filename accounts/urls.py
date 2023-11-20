"""from django.urls import path
from .views import PetSeekerListCreateView, PetShelterListCreateView, UserStoresListCreate


app_name="accounts"

urlpatterns = [
    path('pet-seekers/', PetSeekerListCreateView.as_view(), name='pet-seeker-list-create'),
    path('pet-shelters/', PetShelterListCreateView.as_view(), name='pet-shelter-list-create'),
    path('pet-shelter/', UserStoresListCreate.as_view(), name='pet-list-create'),
    # Add more URLs for updating, retrieving, or deleting pet seekers and pet shelters if needed
]
"""
# accounts/urls.py

from django.urls import path
from .views import UserCreateView, UserRetrieveUpdateDestroy, UserProfileView, ShelterListView, \
    SeekerRetrieveUpdateDestroy, ShelterRetrieveUpdateDestroy, UserDeleteView, CustomTokenObtainPairView,\
    SeekerCreateView, ShelterCreateView, RegisterView, ShelterGetsSeekerView, ShelterRetrieve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #newuser
    #path('create/', UserCreateView.as_view(), name='user-create'),
    path('newuser/', UserCreateView.as_view(), name='user-create'),
    #path('create/seeker/', SeekerCreateView.as_view(), name='seeker-create'),
    path('newuser/seeker/', SeekerCreateView.as_view(), name='seeker-create'),
    #path('create/shelter/', ShelterCreateView.as_view(), name='shelter-create'),
    path('newuser/shelter/', ShelterCreateView.as_view(), name='shelter-create'),
    #user/pk/editor    editor may not be needed
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-update'),
    #seeker/pk/editor
    path('seeker/', SeekerRetrieveUpdateDestroy.as_view(), name='seeker-update'),
    #path('seeker/update/', SeekerRetrieveUpdateDestroy.as_view(), name='seeker-update'),
    #shelter/pk/editor
    path('shelter/', ShelterRetrieveUpdateDestroy.as_view(), name='shelter-update'),
    #path('shelter/update/', ShelterRetrieveUpdateDestroy.as_view(), name='shelter-update'),
    #path('shelter/update/', ShelterRetrieveUpdateDestroy.as_view(), name='shelter-update'),
    path('shelter/<int:pk>/', ShelterRetrieve.as_view(), name='shelter-get'),
    path('shelter/applicant/<int:pk>/', ShelterGetsSeekerView.as_view(), name='shelter-applicant'),
    #user/pk
    path('<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('shelter/<int:shel>/applicant/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('shelters/', ShelterListView.as_view(), name='shelter-list'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('api/newuser/', RegisterView.as_view(), name="sign_up"),
    path('api/user/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #api/user/refreshed_token???
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
