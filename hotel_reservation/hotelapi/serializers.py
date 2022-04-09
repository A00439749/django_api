from rest_framework import serializers
from hotelapi.models import HotelList, Reservation, GuestList


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelList
        fields = ('hotel_name', 'price', 'availability')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('booking_id', 'hotel_name', 'checkin', 'checkout')


class GuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestList
        fields = ('booking_id', 'guest_name', 'guest_gender')
