# Generated by Django 3.1.7 on 2021-03-19 18:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20210320_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 18, 48, 51, 465086, tzinfo=utc)),
        ),
    ]
