from django.contrib import admin
from .models import Device, DeviceData

admin.site.register([Device, DeviceData])