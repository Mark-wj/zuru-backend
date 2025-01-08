from rest_framework import serializers
from .models import User, Category, Destination, Service, Booking, Review, Activity, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class DestinationSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'description', 'location', 'image_url', 'rating', 'category', 'category_id', 'created_at']


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), write_only=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id', 'destination', 'destination_id']


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), write_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'user_id', 'service', 'service_id', 'booking_date', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), write_only=True)
    service = ServiceSerializer(read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), write_only=True, required=False)

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_id', 'destination', 'destination_id', 'service', 'service_id', 'rating', 'comment', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), write_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'category', 'category_id', 'destination', 'destination_id']


class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'booking', 'booking_id', 'amount', 'payment_method', 'payment_date']
