from rest_framework.permissions import BasePermission

class IsNotiOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the owner of the comment
        return obj.user == request.user