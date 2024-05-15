from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Car, Customer, Dealer, Rental


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

