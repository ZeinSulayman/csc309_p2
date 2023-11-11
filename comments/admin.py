from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShelterComments, AppComments
# Register your models here.
#admin.site.register(PetSeeker)
admin.site.register(ShelterComments)
admin.site.register(AppComments)
