# Generated by Django 2.2.13 on 2023-04-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='wallet_amount',
            field=models.IntegerField(default=0),
        ),
    ]
