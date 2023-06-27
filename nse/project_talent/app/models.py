from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.TextField()
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
