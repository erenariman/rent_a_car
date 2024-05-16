from rest_framework import serializers
from .models import Dealer, Car, Customer, Rental
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class DealerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Dealer
        fields = ['user', 'phone_number']


class CarSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'color', 'mileage', 'price_per_day', 'available', 'location', 'dealer']


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rented_cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'rented_cars']


class RentalSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    car = CarSerializer()

    class Meta:
        model = Rental
        fields = ['id', 'customer', 'car', 'rental_date', 'return_date', 'total_price']
