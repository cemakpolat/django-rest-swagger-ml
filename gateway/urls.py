"""
@author: Cem Akpolat
@created by cemakpolat at 2023-04-29
"""

from django.urls import path, include
from rest_framework import routers

from gateway.views import DeviceViewSet, DeviceStatusViewSet, EmployeeViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'devices/(?P<device_id>[^/.]+)/status', DeviceStatusViewSet, basename='devicestatus')

router.register(r'employees', EmployeeViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]