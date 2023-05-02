from django.contrib import admin

from .models import Device, DeviceValue, Employee, Service


admin.site.register(Device)
admin.site.register(DeviceValue)
admin.site.register(Employee)
admin.site.register(Service)