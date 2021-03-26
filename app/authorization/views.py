from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Employees, Customers
from .serializers import  EmployeesSerializer, CustomersSerializer, CustomUserSerializer
from .user_serializers import InfoCustomersSerializer
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # print(CustomUser.objects.get(c_role_info=''))

    @action(detail=False, methods=['get'])
    def me(self, request):
        queryset = CustomUser.objects.filter(email=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    # def get_queryset(self):
    #     return CustomUser.objects.annotate(
    #         role_info=Customers.objects.all()
    #     )

class EmployeesViewSet(ModelViewSet):
    queryset = CustomUser.objects.filter(Q(role='employee') | Q(role='manager'))
    # queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    @action(detail=False, methods=['post'], url_path='import')
    def multiple_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomersViewSet(ModelViewSet):
    # queryset = Customers.objects.all()
    queryset = CustomUser.objects.filter(role='customer')
    serializer_class = CustomersSerializer
