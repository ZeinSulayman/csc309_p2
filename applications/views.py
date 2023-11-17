from .serializers import PetApplicationSerializer
from django.shortcuts import get_object_or_404
from .models import PetApplication
from .serializers import PetApplicationUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsShelter, IsPetSeeker
from rest_framework.pagination import PageNumberPagination
from listings.models import Pet
from accounts.models import PetShelter


class ShelterApplicationsListView(APIView):
    permission_classes = [IsShelter]

    def get(self, request):
        # Retrieve query parameters for status filtering, sorting, and pagination
        status_filter = request.query_params.get('status', None)
        sort_by = request.query_params.get('sort_by', None)

        # Apply pagination
        paginator = PageNumberPagination()
        #applications = PetApplication.objects.filter(pet__shelter=request.user.shelter)
        shelter = PetShelter.objects.filter(user=self.request.user)
        applications = PetApplication.objects.filter(pet_shelter=shelter)
        result_page = paginator.paginate_queryset(applications, request)

        # Apply status filter if provided
        if status_filter:
            result_page = result_page.filter(status=status_filter)

        # Apply sorting if provided
        if sort_by:
            if sort_by == 'created':
                result_page = sorted(result_page, key=lambda x: x.date_created)
            elif sort_by == 'modified':
                result_page = sorted(result_page, key=lambda x: x.last_modified, reverse=True)

        serializer = PetApplicationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PetApplicationUpdateView(APIView):
    permission_classes = [IsShelter | IsPetSeeker]

    def get_object(self, application_id):
        return get_object_or_404(PetApplication, pk=application_id)

    def put(self, request, application_id):
        application = self.get_object(application_id)

        # Check if the user has permission to update the application
        if (request.user.is_pet_shelter and application.PENDING) or \
                (request.user.is_pet_seeker and application.PENDING or application.ACCEPTED):
            serializer = PetApplicationUpdateSerializer(application, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


class PetApplicationDetailView(APIView):
    permission_classes = [IsShelter | IsPetSeeker]

    def get(self, request, application_id):
        application = get_object_or_404(PetApplication, pk=application_id, applicant=request.user)
        serializer = PetApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PetApplicationView(APIView):
    permission_classes = [IsPetSeeker]

    def post(self, request, pet_id):
        pet = Pet.objects.get(pk=pet_id)

        # Check if the pet is available for adoption
        #if not pet.available:
        if not pet.status == 'Available':
            return Response({'error': 'Pet is not available for adoption.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PetApplicationSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save(pet=pet, applicant=request.user)
            serializer.save(applicant=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)