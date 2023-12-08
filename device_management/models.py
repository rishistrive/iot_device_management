from django.db import models
from django.utils.timezone import now
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager

from accounts.models import User


class Device(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="devices")
    manufacturer = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - manufactured by {self.manufacturer}"


class TimescaleModel(models.Model):
    time = TimescaleDateTimeField(interval="1 day", default=now)
    objects = TimescaleManager()

    class Meta:
        abstract = True


class DeviceData(TimescaleModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="data")
    value = models.CharField(blank=True, null=True)

    def __str__(self):
        return f"{self.device.name}"
