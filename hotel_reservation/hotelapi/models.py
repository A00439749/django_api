from django.db import models


# Create your models here.
class HotelList(models.Model):
    hotel_name = models.CharField(max_length=120, primary_key=True)
    price = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)


class Reservation(models.Model):
    booking_id = models.AutoField(primary_key=True)
    hotel_name = models.ForeignKey(HotelList, on_delete=models.CASCADE)
    checkin = models.CharField(max_length=120)
    checkout = models.CharField(max_length=120)


class GuestList(models.Model):
    booking_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=120)
    guest_gender = models.CharField(max_length=30)
