from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Add any other fields you need

    def __str__(self):
        return self.username
