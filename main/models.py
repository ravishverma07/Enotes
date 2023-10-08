from django.db import models
from authsystem.models import CustomUser
from allauth.socialaccount.models import SocialAccount


class Note(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.CharField(max_length=100,default=None)
    pdf_file = models.FileField(upload_to='pdfs/')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=None)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title




class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    def __str__(self):
       return f'Feedback from {self.user}'
           