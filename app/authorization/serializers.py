from rest_framework import serializers

from .models import CustomUser, Employees

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)
        # fields = '__all__'


class EmployeesListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        employees = [Employees(**item) for item in validated_data]
        return Employees.objects.bulk_create(employees)

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        list_serializer_class = EmployeesListSerializer
        fields = '__all__'