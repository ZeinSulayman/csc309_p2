from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from applications.models import PetApplication

class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the owner of the comment
        return obj.user == request.user

class IsShelterOwner(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is associated with the shelter
        shelter_id = view.kwargs.get('shelter_id')  # Adjust based on your URL pattern
        user = request.user
        if request.user.is_pet_seeker == True:
            print("reached")
            return True

        # Add your logic to check if the user is associated with the shelter
        # For example, if you have a ForeignKey from User to Shelter, you can check:
        #return user.PetShelter_set.filter(id=shelter_id).exists()
        print(hasattr(user, 'pet_shelter'))
        print(user.pet_shelter.shelter_id)
        print(shelter_id)
        return hasattr(user, 'pet_shelter') and user.pet_shelter.shelter_id == shelter_id

class IsAppOwner(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is associated with the shelter
        app_id = view.kwargs.get('application_id')  # Adjust based on your URL pattern
        user = request.user
        """print(hasattr(user, 'PetApplication'))
        print(user.PetApplication.app_id)
        print(app_id)"""
        app = get_object_or_404(PetApplication, id=app_id)
        return app.applicant == user
        #return hasattr(user, 'application') and user.application.app_id == app_id