from rest_framework import permissions


class IsShelter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_pet_shelter


class IsPetSeeker(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_pet_seeker
