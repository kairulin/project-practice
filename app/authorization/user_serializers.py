from rest_framework import serializers

from .models import  CustomUser,Employees, Customers


class InfoEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        read_only_fields = ('id','user')

class InfoCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        read_only_fields = ('id','user')
