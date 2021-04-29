from rest_framework.routers import SimpleRouter

from app.authorization import views  as authorization_views

router = SimpleRouter()

router.register('users',authorization_views.CustomUserViewSet)
router.register('employees',authorization_views.EmployeesViewSet)
router.register('customers',authorization_views.CustomersViewSet)