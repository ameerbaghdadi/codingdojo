# Generated by Django 2.2.4 on 2022-10-01 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0002_show_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='releasedate',
            field=models.DateField(default=datetime.date(2022, 10, 1)),
        ),
    ]
