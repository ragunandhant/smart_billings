# Generated by Django 2.2.13 on 2023-04-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20230408_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_preorder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
