
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Device, Employee, Service, DeviceValue, DeviceStatus
from drf_spectacular.utils import extend_schema
from .serializer import DeviceSerializer, DeviceStatusSerializer, DeviceValueSerializer, EmployeeSerializer, ServiceSerializer
from drf_spectacular.utils import extend_schema_view, OpenApiParameter


@extend_schema(tags=['Devices'])
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['get'])
    def values(self, request, pk=None):
        device = self.get_object()
        values = DeviceValue.objects.filter(device=device)
        serializer = DeviceValueSerializer(values, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def addvalue(self, request, pk=None):
        device = self.get_object()
        if "device" not in request.data:
            request.data['device'] = device.id
        value_serializer = DeviceValueSerializer(data=request.data)
        value_serializer.is_valid(raise_exception=True)
        value_serializer.save()

        return Response(value_serializer.data)


@extend_schema_view(
   list=extend_schema(tags=["Employees"]),
   update=extend_schema(exclude=True),
)
@extend_schema(tags=['Employees'])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(tags=['Services'])
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@extend_schema(tags=['Device Status'])
class DeviceStatusViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceStatusSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs.get('device_id')
        queryset = DeviceStatus.objects.filter(device=device_id)
        return queryset