from rest_framework import serializers
from .models import Device, DeviceStatus, DeviceValue, Employee, Service


class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = ['id', 'status', 'average_value', 'prediction']


class DeviceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceValue
        fields = ['id',  'timestamp', 'temperature', 'humidity']


class DeviceSerializer(serializers.ModelSerializer):
    statistics = DeviceStatusSerializer(many=False, read_only=True)
    values = DeviceValueSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'serial_number','location','status', 'values', 'statistics']


class EmployeeSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = ['id', 'device', 'status', 'average_value', 'prediction']