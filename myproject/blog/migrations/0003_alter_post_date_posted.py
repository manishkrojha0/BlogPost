# Generated by Django 4.0.3 on 2022-03-24 04:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 24, 4, 51, 1, 297700, tzinfo=utc)),
        ),
    ]
