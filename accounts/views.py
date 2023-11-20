# accounts/views.py

from rest_framework import generics,views
from .models import User, PetSeeker, PetShelter
from applications.models import PetApplication
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, PetSeekerSerializer, PetShelterSerializer
from .permissions import IsShelter, IsPetSeeker
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import permissions

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return get_object_or_404(User, id=self.kwargs['pk'])

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShelterListView(generics.ListAPIView):
    queryset = PetShelter.objects.all()
    #serializer_class = UserSerializer
    #def get_queryset(self):
    #    return PetShelter.objects.filter(user=self.request.user)
    serializer_class = PetShelterSerializer

class PetSeekerListView(generics.ListAPIView):
    queryset = PetSeeker.objects.all()
    #queryset = User.objects.filter(is_pet_seeker=True)
    #serializer_class = UserSerializer
    #def get_queryset(self):
    #    return PetSeeker.objects.filter(user=self.request.user)
    serializer_class = PetSeekerSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsShelter | IsPetSeeker]

class SeekerCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsPetSeeker]
    #queryset = PetSeeker.objects.all()
    serializer_class = PetSeekerSerializer

    def get_queryset(self):
        #if self.request.user.application.id
        #if Application.objects.filter(user=self.request.user).exists():
            return PetSeeker.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return PetSeeker.objects.create(**serializer.validated_data, user=self.request.user)
        #store.save()

class SeekerUpdateView(generics.UpdateAPIView):
    def get_queryset(self):
        return PetSeeker.objects.filter(user=self.request.user)

class SeekerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetSeekerSerializer
    permission_classes = [IsPetSeeker]
    def get_object(self):
        return get_object_or_404(PetSeeker, user=self.request.user)

    def perform_destroy(self, instance):
        user_id = instance.user.id
        User.objects.filter(id=user_id).delete()
        instance.delete()

class ShelterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetShelterSerializer
    permission_classes = [IsShelter]
    def get_object(self):
        return get_object_or_404(PetShelter, user=self.request.user)

    def perform_destroy(self, instance):
        user_id = instance.user.id
        User.objects.filter(id=user_id).delete()
        instance.delete()

class ShelterCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsShelter]
    #queryset = PetShelter.objects.all()
    serializer_class = PetShelterSerializer

    def get_queryset(self):
        return PetShelter.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        PetShelter.objects.create(**serializer.validated_data, user=self.request.user)
        #PetShelter.save()

#this probably doesnt work and needs to be fixed
class ShelterGetsSeekerView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsShelter]
    serializer_class = PetSeekerSerializer
    def get_object(self):
        seeker = get_object_or_404(User, id=self.kwargs['pk'])
        app = get_object_or_404(PetApplication, applicant = seeker)
        if app.status == "pending":
            return get_object_or_404(PetSeeker, user = seeker)
    """def get_queryset(self):
        seeker = User.objects.filter(id = self.kwargs['pk'])
        return seeker"""
        #if seeker.application.status == "pending" and seeker.application.shelter_id == self.kwargs['shel'] :
        #if seeker.PetApplication_set.all() and seeker.PetApplication_set.user == self.request.user:
            #return PetSeeker.objects.filter(user=self.request.user)


class ShelterRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetShelterSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return get_object_or_404(PetShelter,shelter_id = self.kwargs['pk'])

# view for registering users
class RegisterView(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
