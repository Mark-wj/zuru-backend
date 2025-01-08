from django.urls import path
from .views import (
    UserListCreateAPIView, 
    UserRetrieveUpdateDestroyAPIView, 
    CategoryListCreateAPIView, 
    CategoryRetrieveUpdateDestroyAPIView,
    DestinationListCreateAPIView,
    DestinationRetrieveUpdateDestroyAPIView,
    ServiceListCreateAPIView,
    ServiceRetrieveUpdateDestroyAPIView,
    BookingListCreateAPIView,
    BookingRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
    ActivityListCreateAPIView,
    ActivityRetrieveUpdateDestroyAPIView,
    PaymentListCreateAPIView,
    PaymentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # User routes
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    
    # Category routes
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # Destination routes
    path('api/destinations/', DestinationListCreateAPIView.as_view(), name='destination-list-create'),
    path('api/destinations/<int:pk>/', DestinationRetrieveUpdateDestroyAPIView.as_view(), name='destination-detail'),

    # Service routes
    path('api/services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('api/services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),

    # Booking routes
    path('api/bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('api/bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='booking-detail'),

    # Review routes
    path('api/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),

    # Activity routes
    path('api/activities/', ActivityListCreateAPIView.as_view(), name='activity-list-create'),
    path('api/activities/<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(), name='activity-detail'),

    # Payment routes
    path('api/payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]
