from django.db import models

# Create your models here.
from django.db import models
#from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField(verbose_name="website", blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="active",
                                    help_text="disable to hide from customer")
    """owner = models.ForeignKey(User, related_name='stores',
                              null=True, on_delete=models.SET_NULL,
                              blank=True)"""

    def __str__(self):
        return f"{self.name}"