from django.db import models
from datetime import date
from datetime import timedelta

# Create your models here.
class Hotel(models.Model):

    hotel_name = models.CharField(max_length=60)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):

        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


class Reservation(models.Model):

    hotel_name = models.CharField(max_length=60)
    checkin = models.DateField(default=date.today)
    checkout = models.DateField(default=date.today()+timedelta(days=1))
    guest_name = models.CharField(max_length=60, default="John Doe")
    gender = models.CharField(max_length=6)

    def __str__(self):

        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


