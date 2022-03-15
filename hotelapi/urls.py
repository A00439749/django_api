# hotelapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'getListofHotels', views.HotelViewSet, basename="Hotel")
router.register(r'reservationConfirmation', views.HotelViewSet, basename="Hotel")

# API using automatic URL routing.
# include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'getListofHotels', views.HotelViewSet.getListofHotels),
    path(r'reservationConfirmation', views.HotelViewSet.reservationConfirmation),
]
