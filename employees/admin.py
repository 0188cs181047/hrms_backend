from django.contrib import admin
from .models import Employee, Attendance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "department")
    search_fields = ("full_name", "email", "id")
    list_filter = ("department",)
    readonly_fields = ("id",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "status")
    list_filter = ("status", "date", "employee")
    search_fields = ("employee__full_name",)