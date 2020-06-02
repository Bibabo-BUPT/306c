from django.db import models

# Create your models here.
class room(models.Model):
    room_no=models.IntegerField
    temper=models.FloatField
    customer=models.IntegerField
class detailed_list_room(models.Manager):
    date=models.CharField
    time=models.CharField
    room_no=models.IntegerField
    total_fee=models.FloatField
    target_temper=models.FloatField
    speed=models.IntegerField
class main_controller(models.Model):
    default_mode=models.IntegerField
    default_temper=models.IntegerField
    default_speed=models.IntegerField
    feerateL=models.FloatField
    feerateM:float
    feerateH:float