# Generated by Django 3.1.7 on 2021-03-19 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20210319_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 18, 33, 11, 433671, tzinfo=utc)),
        ),
    ]