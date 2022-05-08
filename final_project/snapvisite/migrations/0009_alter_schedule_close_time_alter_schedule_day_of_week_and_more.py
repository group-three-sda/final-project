# Generated by Django 4.0.4 on 2022-05-08 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapvisite', '0008_alter_company_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='close_time',
            field=models.TimeField(choices=[(datetime.time(6, 0), "<class 'datetime.time'>"), (datetime.time(6, 30), "<class 'datetime.time'>"), (datetime.time(7, 0), "<class 'datetime.time'>"), (datetime.time(7, 30), "<class 'datetime.time'>"), (datetime.time(8, 0), "<class 'datetime.time'>"), (datetime.time(8, 30), "<class 'datetime.time'>"), (datetime.time(9, 0), "<class 'datetime.time'>"), (datetime.time(9, 30), "<class 'datetime.time'>"), (datetime.time(10, 0), "<class 'datetime.time'>"), (datetime.time(10, 30), "<class 'datetime.time'>"), (datetime.time(11, 0), "<class 'datetime.time'>"), (datetime.time(11, 30), "<class 'datetime.time'>"), (datetime.time(12, 0), "<class 'datetime.time'>"), (datetime.time(12, 30), "<class 'datetime.time'>"), (datetime.time(13, 0), "<class 'datetime.time'>"), (datetime.time(13, 30), "<class 'datetime.time'>"), (datetime.time(14, 0), "<class 'datetime.time'>"), (datetime.time(14, 30), "<class 'datetime.time'>"), (datetime.time(15, 0), "<class 'datetime.time'>"), (datetime.time(15, 30), "<class 'datetime.time'>"), (datetime.time(16, 0), "<class 'datetime.time'>"), (datetime.time(16, 30), "<class 'datetime.time'>"), (datetime.time(17, 0), "<class 'datetime.time'>"), (datetime.time(17, 30), "<class 'datetime.time'>"), (datetime.time(18, 0), "<class 'datetime.time'>"), (datetime.time(18, 30), "<class 'datetime.time'>"), (datetime.time(19, 0), "<class 'datetime.time'>"), (datetime.time(19, 30), "<class 'datetime.time'>"), (datetime.time(20, 0), "<class 'datetime.time'>"), (datetime.time(20, 30), "<class 'datetime.time'>"), (datetime.time(21, 0), "<class 'datetime.time'>"), (datetime.time(21, 30), "<class 'datetime.time'>"), (datetime.time(22, 0), "<class 'datetime.time'>"), (datetime.time(22, 30), "<class 'datetime.time'>"), (datetime.time(23, 0), "<class 'datetime.time'>"), (datetime.time(23, 30), "<class 'datetime.time'>")]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('tue', 'Tuesday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='mon', max_length=20),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='open_time',
            field=models.TimeField(choices=[(datetime.time(6, 0), "<class 'datetime.time'>"), (datetime.time(6, 30), "<class 'datetime.time'>"), (datetime.time(7, 0), "<class 'datetime.time'>"), (datetime.time(7, 30), "<class 'datetime.time'>"), (datetime.time(8, 0), "<class 'datetime.time'>"), (datetime.time(8, 30), "<class 'datetime.time'>"), (datetime.time(9, 0), "<class 'datetime.time'>"), (datetime.time(9, 30), "<class 'datetime.time'>"), (datetime.time(10, 0), "<class 'datetime.time'>"), (datetime.time(10, 30), "<class 'datetime.time'>"), (datetime.time(11, 0), "<class 'datetime.time'>"), (datetime.time(11, 30), "<class 'datetime.time'>"), (datetime.time(12, 0), "<class 'datetime.time'>"), (datetime.time(12, 30), "<class 'datetime.time'>"), (datetime.time(13, 0), "<class 'datetime.time'>"), (datetime.time(13, 30), "<class 'datetime.time'>"), (datetime.time(14, 0), "<class 'datetime.time'>"), (datetime.time(14, 30), "<class 'datetime.time'>"), (datetime.time(15, 0), "<class 'datetime.time'>"), (datetime.time(15, 30), "<class 'datetime.time'>"), (datetime.time(16, 0), "<class 'datetime.time'>"), (datetime.time(16, 30), "<class 'datetime.time'>"), (datetime.time(17, 0), "<class 'datetime.time'>"), (datetime.time(17, 30), "<class 'datetime.time'>"), (datetime.time(18, 0), "<class 'datetime.time'>"), (datetime.time(18, 30), "<class 'datetime.time'>"), (datetime.time(19, 0), "<class 'datetime.time'>"), (datetime.time(19, 30), "<class 'datetime.time'>"), (datetime.time(20, 0), "<class 'datetime.time'>"), (datetime.time(20, 30), "<class 'datetime.time'>"), (datetime.time(21, 0), "<class 'datetime.time'>"), (datetime.time(21, 30), "<class 'datetime.time'>"), (datetime.time(22, 0), "<class 'datetime.time'>"), (datetime.time(22, 30), "<class 'datetime.time'>"), (datetime.time(23, 0), "<class 'datetime.time'>"), (datetime.time(23, 30), "<class 'datetime.time'>")]),
        ),
    ]
