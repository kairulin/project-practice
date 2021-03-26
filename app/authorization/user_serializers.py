from rest_framework import serializers

from .models import  CustomUser,Employees, Customers


class InfoEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('id',)

class InfoCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('user',)
        # fields = '__all__'
        # read_only_fields = ('id','user',)

# class CustomUserSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()
#
#     role_info = CustomersSerializer()

#     def get_full_name(self, obj):
#         return obj.get_full_name().upper()
#
#     class Meta:
#         model = CustomUser
#         fields = ('uuid', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role', 'role_info')
#         read_only_fields = ('role',)
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'first_name': {'write_only': True},
#             'last_name': {'write_only': True}
#         }