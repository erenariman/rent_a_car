from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, RentalViewSet

router = routers.DefaultRouter()
router.register(r'car', CarViewSet, basename='car')
router.register(r'rental', RentalViewSet, basename='rental')

urlpatterns = router.urls
