# Generated by Django 2.2.13 on 2023-04-08 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
    ]
