from rest_framework import generics
from .models import Pet
from .serializers import PetListSerializer, PetCreateSerializer
from .filters import PetFilter
from rest_framework.pagination import PageNumberPagination
from .permissions import IsShelter, IsShelterOwner
from rest_framework.permissions import IsAuthenticated


class PetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PetCreateView(generics.CreateAPIView):
    permission_classes = [IsShelter]
    serializer_class = PetCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Pet.objects.filter(status='Available')
    filter_class = PetFilter
    pagination_class = PetPagination
    serializer_class = PetListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'name')
        return queryset.order_by(ordering)


class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsShelterOwner]
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer
