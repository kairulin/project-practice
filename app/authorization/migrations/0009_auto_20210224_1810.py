# Generated by Django 3.1.5 on 2021-02-24 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_auto_20210127_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
    ]
