from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .models import Store
from .serializers import AdminStoreSerializer

class AdminStoresListCreate(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminStoreSerializer
    queryset = Store.objects.all()


class AdminStoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminStoreSerializer

    def get_object(self):
        return get_object_or_404(Store, id=self.kwargs['pk'])
