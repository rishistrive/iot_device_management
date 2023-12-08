from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DeviceManagementViewSet, DeviceDataManagementViewSet

router = DefaultRouter()
router.register(r"device", DeviceManagementViewSet, basename="device")
router.register(r"device-data", DeviceDataManagementViewSet, basename="device-data")


urlpatterns = [path("api/", include(router.urls))]
