# Generated by Django 3.1.5 on 2021-01-26 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_employees_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='roler',
        ),
    ]
