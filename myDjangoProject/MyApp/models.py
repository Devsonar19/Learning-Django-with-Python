from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length = 69, default='')
    details = models.CharField(max_length=500, default='')