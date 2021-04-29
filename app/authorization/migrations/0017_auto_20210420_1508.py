# Generated by Django 3.1.5 on 2021-04-20 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0016_auto_20210311_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='customer', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employees',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]