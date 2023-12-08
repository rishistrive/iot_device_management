from rest_framework import serializers
from .models import Device, DeviceData


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "name", "owner", "manufacturer", "description", "created"]
        read_only_fields = ["id"]


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ["device", "value", "time"]
