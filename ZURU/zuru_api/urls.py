from django.urls import path
from .views import (
    DestinationListCreateAPIView,
    DestinationRetrieveUpdateDestroyAPIView,
    ServiceListCreateAPIView,
    ServiceRetrieveUpdateDestroyAPIView,
    ActivityListCreateAPIView,
    ActivityRetrieveUpdateDestroyAPIView,
    UserProfileListCreateAPIView,
    UserProfileRetrieveUpdateDestroyAPIView,
    BookingListCreateAPIView,
    BookingRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # UserProfile routes
    path('zuru/user-profiles/', UserProfileListCreateAPIView.as_view(), name='userprofile-list-create'),
    path('zuru/user-profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='userprofile-detail'),

    #Booking routes
    path('zuru/bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('zuru/bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='booking-detail'),

    # Destination routes
    path('zuru/destinations/', DestinationListCreateAPIView.as_view(), name='destination-list-create'),
    path('zuru/destinations/<int:pk>/', DestinationRetrieveUpdateDestroyAPIView.as_view(), name='destination-detail'),

    # Service routes
    path('zuru/services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('zuru/services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),
    
    # Activity routes
    path('zuru/activities/', ActivityListCreateAPIView.as_view(), name='activity-list-create'),
    path('zuru/activities/<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(), name='activity-detail'),
]
