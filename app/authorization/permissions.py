from rest_framework import permissions
from app.authorization.models import CustomUser

class IsAdminAccount(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.role == 'system' or user.role == 'manager' or user.groups.filter(name='test'):
            return True
        else:
            return user.is_superuser

