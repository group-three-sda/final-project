# Generated by Django 4.0.4 on 2022-06-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirm',
            field=models.BooleanField(default=True),
        ),
    ]
