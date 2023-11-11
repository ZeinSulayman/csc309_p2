# accounts/permissions.py

from rest_framework import permissions

class IsShelter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_pet_shelter

class IsPetSeeker(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_pet_seeker
    """def has_permission(self, request, view):
        # Check if the user is associated with the shelter
        app_id = view.kwargs.get('application_id')  # Adjust based on your URL pattern
        user = request.user
        return request.user.is_authenticated and user.application.app_id == app_id
"""