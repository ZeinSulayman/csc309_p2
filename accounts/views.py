"""from rest_framework import generics
from .models import PetSeeker, PetShelter
from .serializers import PetSeekerSerializer, PetShelterSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class UserStoresListCreate(ListCreateAPIView):
    serializer_class = PetSeekerSerializer

    def get_queryset(self):
        return PetSeeker.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # save the store first (otherwise products won't have a store to refer to)
        store = PetSeeker.objects.create(**serializer.validated_data, owner=self.request.user)

        # for each product in products, create new product
        #for product_data in products:
        #    Product.objects.create(**product_data, store=store)
class PetSeekerListCreateView(generics.ListCreateAPIView):
    queryset = PetSeeker.objects.all()
    serializer_class = PetSeekerSerializer

class PetShelterListCreateView(generics.ListCreateAPIView):
    queryset = PetShelter.objects.all()
    serializer_class = PetShelterSerializer
"""

# accounts/views.py

from rest_framework import generics
from .models import User, PetSeeker, PetShelter
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, PetSeekerSerializer, PetShelterSerializer
from .permissions import IsShelter, IsPetSeeker
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        if user.is_pet_shelter:
            user.is_pet_shelter = True
            pet_shelter_data = request.data.get('pet_shelter', {})
            pet_shelter_serializer = PetShelterSerializer(data=pet_shelter_data)
            pet_shelter_serializer.is_valid(raise_exception=True)
            pet_shelter_serializer.save(user=user)
        elif user.is_pet_seeker:
            user.is_pet_seeker = True
            pet_seeker_data = request.data.get('pet_seeker', {"bio"})
            pet_seeker_serializer = PetSeekerSerializer(data=pet_seeker_data)
            pet_seeker_serializer.is_valid(raise_exception=True)
            pet_seeker_serializer.save(user=user)

        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)"""


"""class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsShelter | IsPetSeeker]"""
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

class ShelterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetShelterSerializer
    permission_classes = [IsShelter]
    def get_object(self):
        return get_object_or_404(PetShelter, user=self.request.user)

class ShelterCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsShelter]
    #queryset = PetShelter.objects.all()
    serializer_class = PetShelterSerializer

    def get_queryset(self):
        return PetShelter.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        PetShelter.objects.create(**serializer.validated_data, user=self.request.user)
        #PetShelter.save()

# view for registering users
class RegisterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

