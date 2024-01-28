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


class Skill(models.Model):
    name = models.TextField(max_length=50)
    def __str__(self):
        return self.name 

class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    heading = models.TextField()
    paragraph = models.TextField(default="")
    question = models.TextField()
    answer = models.TextField()
    def __str__(self) :
        return f'details of {self.skill}'
   

           