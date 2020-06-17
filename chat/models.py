from django.db import models

# Create your models here.
class Message(models.Model):
    body = models.TextField()
    time = models.DateTimeField(default=None)
