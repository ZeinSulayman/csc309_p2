from rest_framework.permissions import BasePermission

class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the owner of the comment
        return obj.user == request.user

class IsShelterOwner(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is associated with the shelter
        shelter_id = view.kwargs.get('shelter_id')  # Adjust based on your URL pattern
        user = request.user

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
        return hasattr(user, 'application') and user.application.app_id == app_id