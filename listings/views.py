from rest_framework import generics
from .models import Pet
from .serializers import PetListSerializer, PetCreateSerializer, PetEditSerializer
from .filters import PetFilter
from rest_framework.pagination import PageNumberPagination
from .permissions import IsShelter, IsShelterOwner
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter
    pagination_class = PetPagination
    serializer_class = PetListSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()

        status_param = self.request.query_params.get('status', 'available')
        if status_param.lower() != 'all':
            queryset = queryset.filter(status=status_param)

        ordering_params = self.request.query_params.getlist('sort')

        if ordering_params:
            queryset = queryset.order_by(*ordering_params, 'name', 'age')
        else:
            queryset = queryset.order_by()

        return queryset

class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsShelterOwner]
    queryset = Pet.objects.all()
    serializer_class = PetEditSerializer
