from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from hotelapi.serializers import HotelListSerializer, ReservationSerializer, GuestListSerializer
from hotelapi.models import HotelList, Reservation, GuestList


class HotelListViewSet(viewsets.ModelViewSet):
   queryset = HotelList.objects.all()
   serializer_class = HotelListSerializer


class ReservationViewSet(viewsets.ModelViewSet):
   queryset = Reservation.objects.all()
   serializer_class = ReservationSerializer


class GuestListViewSet(viewsets.ModelViewSet):
   queryset = GuestList.objects.all()
   serializer_class = GuestListSerializer
