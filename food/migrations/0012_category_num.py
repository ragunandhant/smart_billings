# Generated by Django 2.2.13 on 2023-04-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20230410_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
