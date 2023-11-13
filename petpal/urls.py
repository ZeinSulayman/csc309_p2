from django.urls import path
from . import views

urlpatterns = [
    path('super/stores/', views.AdminStoresListCreate.as_view()),
    path('super/stores/<int:pk>/', views.AdminStoresRetrieveUpdateDestroy.as_view()),
]
