from django.db import models

class Image(models.Model):
    sid=models.CharField(max_length=255)
    time=models.CharField(max_length=13)


# Create your models here.
