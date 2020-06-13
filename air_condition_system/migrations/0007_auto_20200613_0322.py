# Generated by Django 2.2 on 2020-06-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_condition_system', '0006_auto_20200612_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_time', models.IntegerField(default=0)),
                ('open_time', models.IntegerField(default=0)),
                ('change_temper_time', models.IntegerField(default=0)),
                ('change_speed_time', models.IntegerField(default=0)),
                ('room_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='money',
            name='Dmoney',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Name',
        ),
        migrations.AddField(
            model_name='record',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sub_controller_db',
            name='is_out_queue',
            field=models.BooleanField(default=True),
        ),
    ]