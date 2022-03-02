from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HotelSerializer
from .models import Hotel

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all().order_by("hotel_name")
    serializer_class = HotelSerializer
