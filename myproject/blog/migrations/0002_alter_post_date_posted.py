# Generated by Django 4.0.3 on 2022-03-24 04:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 24, 4, 50, 30, 444094, tzinfo=utc)),
        ),
    ]
