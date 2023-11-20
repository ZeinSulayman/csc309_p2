from rest_framework.permissions import IsAuthenticated

from .serializers import PetApplicationSerializer, PetApplicationDetailSerializer, \
    PetApplicationShelterUpdateSerializer, PetApplicationSeekerUpdateSerializer
from django.shortcuts import get_object_or_404
from .models import PetApplication
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsShelter, IsPetSeeker
from rest_framework.pagination import PageNumberPagination
from listings.models import Pet
from accounts.models import PetShelter


class ShelterApplicationsListView(ListAPIView):
    permission_classes = [IsShelter]
    serializer_class = PetApplicationSerializer

    def get_queryset(self):
        # Retrieve query parameters for status filtering, sorting, and pagination
        status_filter = self.request.query_params.get('status', None)
        sort_by = self.request.query_params.get('sort_by', None)


        # Apply status filter if provided
        queryset = PetApplication.objects.filter(pet__owner=self.request.user)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        queryset = queryset.order_by('date_created')
        queryset = queryset.order_by('-last_modified')
        # Apply sorting if provided
        """if sort_by:
            if sort_by == 'created':
                queryset = queryset.order_by('date_created')
            elif sort_by == 'modified':
                queryset = queryset.order_by('-last_modified')"""

        return queryset

    def list(self, request, *args, **kwargs):
        # Apply pagination
        paginator = PageNumberPagination()
        applications = self.get_queryset()
        result_page = paginator.paginate_queryset(applications, request)

        serializer = PetApplicationDetailSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PetApplicationUpdateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, application_id):
        return get_object_or_404(PetApplication, pk=application_id)

    def get_serializer_class(self):
        # Determine the user type and return the appropriate serializer class
        if self.request.user.is_pet_shelter:
            return PetApplicationShelterUpdateSerializer
        elif self.request.user.is_pet_seeker:
            return PetApplicationSeekerUpdateSerializer
        # Add more cases for other user types if needed
        else:
            # Use a default serializer class or raise an exception
            return PetApplicationShelterUpdateSerializer

    def create(self, request, application_id, *args, **kwargs):
        application = self.get_object(application_id)

        # Check if the user has permission to update the application
        if (request.user.is_pet_shelter and application.status == "pending") or \
                (request.user.is_pet_seeker and application.status in ["pending", "accepted"]):
            # Get the appropriate serializer class based on user type
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(application, data=request.data)


            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


class PetApplicationDetailView(APIView):
    permission_classes = [IsShelter | IsPetSeeker]

    def get(self, request, application_id):
        application = get_object_or_404(PetApplication, pk=application_id, applicant=request.user)
        serializer = PetApplicationDetailSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PetApplicationView(CreateAPIView):
    serializer_class = PetApplicationSerializer
    permission_classes = [IsAuthenticated, IsPetSeeker]

    def create(self, request, *args, **kwargs):
        pet_id = self.kwargs.get('pet_id')
        pet = Pet.objects.get(pk=pet_id)

        # Check if the pet is available for adoption
        if not pet.status == 'available':
            return Response({'error': 'Pet is not available for adoption.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, pet)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, pet):
        serializer.save(pet=pet, applicant=self.request.user, status="pending")
