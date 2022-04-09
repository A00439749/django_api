from django.urls import include, path

from rest_framework import routers

from hotelapi.views import HotelListViewSet, ReservationViewSet, GuestListViewSet

router = routers.DefaultRouter()
router.register(r'getlistofhotels', HotelListViewSet)
router.register(r'reservationconfirmation', ReservationViewSet)
router.register(r'guestlist', GuestListViewSet)

urlpatterns = [
   path('', include(router.urls)),
]