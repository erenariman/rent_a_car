from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from serializers import CarSerializer, RentalSerializer
from models import Car, Rental


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

