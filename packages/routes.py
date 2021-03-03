from rest_framework.routers import DefaultRouter

from app.authorization import views  as authorization_views

router = DefaultRouter()

router.register('customuser',authorization_views.CustomUserViewSet)
router.register('employees',authorization_views.EmployeesViewSet)