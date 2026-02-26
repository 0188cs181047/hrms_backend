from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = {
        'department': ['exact'],
        'email': ['exact'],
    }

    search_fields = ['full_name', 'email']


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = {
        'status': ['exact'],
        'employee__department': ['exact'],
        'employee__email': ['exact'],
    }

    search_fields = ['employee__full_name', 'employee__email']