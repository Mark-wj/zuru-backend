from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Activity, Destination, Service, UserProfile, Booking

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'profile_picture', 'phone_number', 'address', 'bio', 'date_of_birth']
        read_only_fields = ['user']  # Prevent direct modification of the `user` field


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__' 


class BookingSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)
    activities = serializers.PrimaryKeyRelatedField(queryset=Activity.objects.all(), many=True)
    destination = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user', 'destination', 'services', 'activities', 'booking_date', 'start_date', 'end_date', 'total_price']
        read_only_fields = ['total_price']  # total_price should be calculated automatically