from django.db import models
from accounts.models import User, PetShelter


class PetApplication(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('withdrawn', 'Withdrawn'),
        ('denied', 'Denied'),
        ('accepted', 'Accepted'),
    ]
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    hours_away_weekdays = models.CharField(max_length=255)
    hours_away_weekends = models.CharField(max_length=255)
    health = models.CharField(max_length=255)
    criminal_history = models.CharField(max_length=255)
    previous_pet = models.BooleanField()
    description = models.CharField(max_length=255)

    pet = models.ForeignKey("listings.Pet", on_delete=models.CASCADE)

    PENDING = models.BooleanField(default=True)
    ACCEPTED = models.BooleanField(default=False)
    DENIED = models.BooleanField(default=False)
    WITHDRAWN = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
