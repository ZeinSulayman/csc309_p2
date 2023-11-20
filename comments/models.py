from django.db import models
# from p2test.accounts.models import User, PetShelter, Application


class AppComments(models.Model):
    content = models.TextField()
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    #app = models.ForeignKey("accounts.Application", on_delete=models.CASCADE)
    app = models.ForeignKey("applications.PetApplication", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ShelterComments(models.Model):
    content = models.TextField()
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    shelter = models.ForeignKey("accounts.PetShelter", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)









"""
class PetSeeker(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pet_seeker')
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(User, related_name='seeker',
                              null=True, on_delete=models.SET_NULL,
                              blank=True)
    # Add other fields specific to pet seekers (e.g., address, phone number, etc.)

class PetShelter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pet_shelter')
    # Add other fields specific to pet shelters (e.g., location, shelter name, etc.)
"""
