from rest_framework import viewsets
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import HotelSerializer
from .serializers import ReservationSerializer
from .models import Hotel
from rest_framework.decorators import api_view

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    # queryset = Hotel.objects.all().order_by("hotel_name")
    serializer_class = ''
    queryset = ''

    @api_view(['GET'])
    def getListofHotels(self):
        # if request.method == "GET":
        queryset = Hotel.objects.all().order_by("hotel_name")
        hotel_serializer = HotelSerializer(queryset, many=True)
        return JsonResponse(hotel_serializer.data, safe=False)

    @api_view(['GET', 'POST'])
    def reservationConfirmation(self, request):
        if request.method == "POST":
            booking_data = JSONParser().parse(request)
            reservation_serializer = ReservationSerializer(data=booking_data)
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return JsonResponse(reservation_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
