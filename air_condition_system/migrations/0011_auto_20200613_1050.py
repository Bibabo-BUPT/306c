# Generated by Django 2.2 on 2020-06-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_condition_system', '0010_remove_money_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='Lmoney',
            field=models.FloatField(max_length=100, verbose_name='累计金额'),
        ),
    ]
