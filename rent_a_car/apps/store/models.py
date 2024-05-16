from django.db import models
from django.contrib.auth.models import User


class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, related_name='dealer_cars', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)
    rented_cars = models.ManyToManyField(Car, through='Rental')

    def __str__(self):
        return self.user.username


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.customer} rented {self.car} on {self.rental_date}"
