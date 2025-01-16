from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destination_images')
    location = models.CharField(max_length=200)
    rating = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activity_images')
    destination = models.ManyToManyField(Destination, related_name='activities')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images')
    destination = models.ManyToManyField(Destination, related_name='services')
    price = models.FloatField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='bookings')
    services = models.ManyToManyField(Service, blank=True, related_name='bookings')
    activities = models.ManyToManyField(Activity, blank=True, related_name='bookings')
    booking_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.FloatField()

    def calculate_total_price(self):
        service_price = sum(service.price for service in self.services.all())
        return service_price

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name} ({self.start_date} to {self.end_date})"
