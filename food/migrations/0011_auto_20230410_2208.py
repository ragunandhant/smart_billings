# Generated by Django 2.2.13 on 2023-04-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20230410_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]