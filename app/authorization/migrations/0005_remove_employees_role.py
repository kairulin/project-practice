# Generated by Django 3.1.5 on 2021-01-27 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_remove_customuser_roler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='role',
        ),
    ]