from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.hotel_name

