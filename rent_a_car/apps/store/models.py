from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)


class Customer(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rented_cars = models.ManyToManyField(Car, through='Rental')

    def __str__(self):
        return self.user_profile.user.username


class Dealer(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    managed_cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.user_profile.user.username


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"{self.customer} rented {self.car} on {self.rental_date}"
