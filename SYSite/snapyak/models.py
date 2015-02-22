from django.db import models

class Image(models.Model):
    sid=models.CharField(max_length=255)
    time=models.CharField(max_length=13)
    path = models.CharField(max_length=255)
    ordering=['-time']
    def __str__(self):
        return str(self.time)



# Create your models here.
