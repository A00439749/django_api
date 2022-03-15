# serializers.py

from rest_framework import serializers

from .models import Hotel
from .models import Reservation

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_name', 'price', 'availability')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('hotel_name', 'checkin', 'checkout', 'guest_name', 'gender')