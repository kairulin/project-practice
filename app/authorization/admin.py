from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Customers, Employees

import csv
from django.http import HttpResponse


def csv_user(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    titles = ['id', 'role', '中文姓名', '最後登入時間', '加入時間']
    writer.writerow(titles)

    users = queryset.values_list('id', 'role', 'last_login', 'date_joined')
    for user in users:
        writer.writerow(user)
    return response


csv_user.short_description = '匯出csv'


class CustomersTabularInline(admin.TabularInline):
    model = Customers


class EmployeesTabularInline(admin.TabularInline):
    model = Employees
    # readonly_fields = ['id']

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'role')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    actions = [
        csv_user,
    ]

    inlines = [
        CustomersTabularInline,
        EmployeesTabularInline
    ]

    class Media:
        js = ('app/formset_handlers.js',)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
