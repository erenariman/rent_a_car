from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import DealerSerializer, CarSerializer, CustomerSerializer, RentalSerializer
from .models import Car, Rental, Customer, Dealer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Car.objects.all()


class RentalViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rental.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all()


class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dealer.objects.all()
