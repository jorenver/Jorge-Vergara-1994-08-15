# Generated by Django 3.0.8 on 2021-04-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercurrency',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
