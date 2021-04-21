from django.db import models

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    expired = models.BooleanField(default=False)