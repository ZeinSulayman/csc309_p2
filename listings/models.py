from django.db import models
#from ..accounts.models import User, PetShelter, PetSeeker


class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    breed = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='available')
    pic = models.ImageField(upload_to='pet_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}'s listing"
