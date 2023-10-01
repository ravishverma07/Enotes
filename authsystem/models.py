from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=60,default='') 
    email = models.EmailField(max_length=255)
    profile_photo_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username 
