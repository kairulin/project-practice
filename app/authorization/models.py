import uuid

from functools import partial

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from app.utils.number import make_user_number
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
     for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Roles(models.TextChoices):
    CUSTOMER = 'customer', '顧客'
    EMPLOYEE = 'employee', '員工'
    MANAGER = 'manager', '管理者'
    SYSTEM = 'system', '系統'


class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    role = models.CharField('角色', max_length=20, choices=Roles.choices, default=Roles.MANAGER)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Customers(models.Model):
    id = models.CharField('員工編號', max_length=100, default=partial(make_user_number, 'C'), unique=True)
    user = models.OneToOneField('CustomUser', primary_key=True, on_delete=models.CASCADE,related_name='customer')
    create_at = models.DateTimeField('建立日期', auto_now_add=True)
    update_at = models.DateTimeField('更新日期', auto_now=True)

    def clean(self, *args, **kwargs):
        if self.user.role == 'manager' or self.user.role == 'employee':
            raise ValidationError('這個User已經在Employees裡存在')
        super(Customers, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Customers, self).save(*args, **kwargs)


class Employees(models.Model):
    id = models.CharField('員工編號', max_length=100, default=partial(make_user_number, 'E'), unique=True)
    user = models.OneToOneField('CustomUser', primary_key=True, on_delete=models.CASCADE,related_name='employee')
    create_at = models.DateTimeField('建立日期', auto_now_add=True)
    update_at = models.DateTimeField('更新日期', auto_now=True)

    def clean(self, *args, **kwargs):
        if self.user.role == 'customer':
            raise ValidationError('這個User已經在Customers裡存在')
        super(Employees, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Employees, self).save(*args, **kwargs)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

