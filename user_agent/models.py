from django.db import models

# Create your models here.

class UserAgentTrack(models.Model):
    count = models.IntegerField()
    user_agent = models.TextField()
