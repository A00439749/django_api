# serializers.py

from rest_framework import serializers

from .models import Hotel

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_name', )
