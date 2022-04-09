from django.contrib import admin
from hotelapi.models import HotelList, Reservation, GuestList

admin.site.register(HotelList)
admin.site.register(Reservation)
admin.site.register(GuestList)
