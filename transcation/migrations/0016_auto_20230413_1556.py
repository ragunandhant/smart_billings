# Generated by Django 2.2.13 on 2023-04-13 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcation', '0015_auto_20230411_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcation',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
    ]
