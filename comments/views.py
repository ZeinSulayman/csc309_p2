from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import AppComments, ShelterComments
from .serializers import AppCommentSerializer, ShelterCommentSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsShelterOwner, IsAppOwner
from rest_framework.pagination import PageNumberPagination
from accounts.models import PetShelter
from applications.models import PetApplication
from django.utils import timezone
#from .permissions import IsCommentOwner

class PetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ShelterCommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PetPagination

    def get_queryset(self):
        # Filter comments based on the specific shelter or pet seeker
        shelter_id = self.kwargs.get('shelter_id')  # Adjust based on your URL pattern
        queryset = ShelterComments.objects.filter(shelter=shelter_id)
        queryset = queryset.order_by('-created_at')
        return queryset
    '''not sure if it should be shelter or shelter_id on the LHS'''


    def perform_create(self, serializer):
        # Automatically set the user based on the logged-in user
        shelter_id = self.kwargs.get('shelter_id')
        shelter = get_object_or_404(PetShelter, shelter_id=shelter_id)
        serializer.save(user=self.request.user, shelter=shelter)

    serializer_class = ShelterCommentSerializer

##need to make sure permissions work
class AppCommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsShelterOwner, IsAppOwner]
    pagination_class = PetPagination

    def get_queryset(self):
        # Filter comments based on the specific shelter or pet seeker
        application_id = self.kwargs.get('application_id')  # Adjust based on your URL pattern
        queryset =  AppComments.objects.filter(app_id=application_id)
        queryset = queryset.order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        # Automatically set the user based on the logged-in user
        application_id = self.kwargs.get('application_id')
        application = get_object_or_404(PetApplication, id=application_id)
        application.last_modified = timezone.now()
        application.save()
        #application = get_object_or_404(Application, user=self.request.user)
        serializer.save(user=self.request.user, app=application)
        #serializer.save(user=self.request.user)

    serializer_class = AppCommentSerializer