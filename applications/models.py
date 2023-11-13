from django.db import models
from accounts.models import User


class PetApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=10)
    occupation = models.CharField(max_length=10)
    hours_away_weekdays = models.CharField(max_length=10)
    hours_away_weekends = models.CharField(max_length=10)
    health = models.CharField(max_length=10)
    criminal_history = models.CharField(max_length=10)
    previous_pet = models.BooleanField()
    description = models.CharField(max_length=10)

    #pet = models.ForeignKey()
    PENDING = models.BooleanField(default=True)
    ACCEPTED = models.BooleanField(default=False)
    DENIED = models.BooleanField(default=False)
    WITHDRAWN = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)


