from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from permission.custom_device_permission import DevicePermission


from .models import Device, DeviceData
from .serializer import DeviceDataSerializer, DeviceSerializer


class DeviceManagementViewSet(ModelViewSet):
    """
    Viewset for managing Device instances.
    """
    permission_classes = [IsAuthenticated, DevicePermission]

    def get_queryset(self):
        queryset = Device.objects.select_related("owner")
        return queryset

    def get_serializer_class(self):
        return DeviceSerializer


class DeviceDataManagementViewSet(ModelViewSet):
    """
    Viewset for managing DeviceData instances.
    """
    permission_classes = [IsAuthenticated, DevicePermission]

    def get_queryset(self):
        queryset = DeviceData.objects.select_related("device")
        return queryset

    def get_serializer_class(self):
        return DeviceDataSerializer
