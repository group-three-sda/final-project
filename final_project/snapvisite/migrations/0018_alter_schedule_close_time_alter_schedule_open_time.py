# Generated by Django 4.0.4 on 2022-05-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapvisite', '0017_merge_20220518_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='open_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
