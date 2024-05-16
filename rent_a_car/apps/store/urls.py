from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, RentalViewSet, DealerViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'car', CarViewSet, basename='car')
router.register(r'rental', RentalViewSet, basename='rental')
router.register(r'dealers', DealerViewSet, basename='dealer')
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = router.urls
