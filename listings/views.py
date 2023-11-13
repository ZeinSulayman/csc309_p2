from rest_framework import generics
from .models import Pet
from .serializers import PetListSerializer, PetCreateSerializer
from .filters import PetFilter
from rest_framework.pagination import PageNumberPagination


class PetPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.filter()
    filter_class = PetFilter
    pagination_class = PetPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetListSerializer
        elif self.request.method == 'POST':
            return PetCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'name')
        return queryset.order_by(ordering)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer
