# Generated by Django 2.2 on 2020-06-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_condition_system', '0003_auto_20200611_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='DeDu',
        ),
        migrations.AddField(
            model_name='sub_controller_db',
            name='bottom_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sub_controller_db',
            name='top_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='Room',
            field=models.IntegerField(verbose_name='房间号'),
        ),
    ]
