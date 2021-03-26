from rest_framework import serializers

from .models import CustomUser, Employees, Customers
from .user_serializers import InfoCustomersSerializer,InfoEmployeesSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    role_info = serializers.SerializerMethodField()
    # c_role_info = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    print('yo')
    print(CustomUser)
    # print(c_role_info)
    # e_role_info = InfoEmployeesSerializer()

    def get_full_name(self, obj):
        return obj.get_full_name().upper()

    def get_role_info(self,obj):
        # print(InfoCustomersSerializer(obj.c_role_info).data)
        print(CustomUserSerializer().data)
        # print(self.c_role_info)
        role_info = obj.role

        return role_info
        # print(InfoCustomersSerializer())
    class Meta:
        model = CustomUser
        fields = ('uuid', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role','role_info','c_role_info','e_role_info')
        read_only_fields = ('role',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True}
        }

class EmployeesListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        # employees = [CustomUser(role='employee',**item) for item in validated_data]
        user_data = []
        for item in validated_data:
            user = CustomUser(
                **item,
                role='employee'
            )
            user.set_password(item['password'])
            user_data.append(user)
        CustomUser.objects.bulk_create(user_data)
        for item in user_data:
            Employees.objects.create(user=item)
        # Employees.objects.bulk_create(user=user_data)
        return user_data

class EmployeesSerializer(serializers.ModelSerializer):

    # user = CustomUserSerializer()
    #
    # class Meta:
    #     model = Employees
    #     fields = '__all__'
    #     read_only_fields = ('id',)
    #
    # def create(self, validated_data):
    #     user_data = validated_data['user']
    #     user_data = CustomUser.objects.create(**user_data, role='employee')
    #     user_data.set_password(user_data.password)
    #     user_data.save()
    #     instance = Employees.objects.create(user=user_data)
    #     return instance
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name().upper()

    class Meta:
        model = CustomUser
        list_serializer_class = EmployeesListSerializer

        fields = ('uuid', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role')
        read_only_fields = ('role',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True}
        }

    def create(self, validated_data):
        user_data = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role='employee',
        )
        user_data.set_password(validated_data['password'])
        user_data.save()
        Employees.objects.create(user=user_data)
        return user_data


class CustomersSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()


    def get_full_name(self, obj):
        return obj.get_full_name().upper()

    class Meta:
        model = CustomUser
        # fields = ('user',)
        fields = ('uuid', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role',)
        read_only_fields = ('role',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True}
        }

    def create(self, validated_data):
        user_data = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role='customer'
        )
        user_data.set_password(validated_data['password'])
        user_data.save()

        Customers.objects.create(user=user_data)
        return user_data

    # from .user_serializers import CustomUserSerializer
    # user = CustomUserSerializer()
    # class Meta:
    #     model = Customers
    #     fields = '__all__'
    #     read_only_fields = ('id',)
    #
    # def create(self,validated_data):
    #     user_data = validated_data['user']
    #     user_data = CustomUser.objects.create(**user_data, role='customer')
    #     user_data.set_password(user_data.password)
    #     user_data.save()
    #
    #     instance = Customers.objects.create(user=user_data)
    #     return instance
