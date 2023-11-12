from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_pet_shelter = models.BooleanField(default=False)
    is_pet_seeker = models.BooleanField(default=False)

    # Add a unique related_name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        related_query_name='user_custom',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Add a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_custom',
        related_query_name='user_permissions_custom',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class PetShelter(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, primary_key=True, related_name="pet_shelter"
    )
    shelter_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s PetShelter Profile"


class PetSeeker(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, primary_key=True, related_name="pet_seeker"
    )
    location = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s PetShelter Profile"


class Pet(models.Model):
    owner = models.OneToOneField(
        'User', on_delete=models.CASCADE, primary_key=True, related_name="pet"
    )
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return f"{self.name}'s listing"
