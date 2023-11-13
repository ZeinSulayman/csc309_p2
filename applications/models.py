from django.db import models
from accounts.models import User


class PetApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField()
    last_name = models.CharField()
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField()
    occupation = models.CharField()
    hours_away_weekdays = models.CharField()
    hours_away_weekends = models.CharField()
    health = models.CharField()
    criminal_history = models.CharField()
    previous_pet = models.BooleanField()
    description = models.CharField()

    pet = models.ForeignKey()
    PENDING = models.BooleanField(default=True)
    ACCEPTED = models.BooleanField(default=False)
    DENIED = models.BooleanField(default=False)
    WITHDRAWN = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)


