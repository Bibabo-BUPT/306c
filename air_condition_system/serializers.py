from rest_framework import serializers,viewsets,filters
from . import models
from django.db.models import Sum

class UserSerializers(serializers.ModelSerializer):
    """用户"""
    class Meta:
        model=models.User
        fields='__all__'

class RecordSerializers(serializers.ModelSerializer):
    """记录"""
    StateDeta=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)#开机时间
    LeaveDeta=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)#关机时间
    Date=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)#最后修改时间
    Room=serializers.CharField(source='Room.Room',read_only=True)#房间号

    class Meta:
        model=models.Record
        fields=('id','Room','DeDu','DangDu','Pattern','Speed','State','StateDeta','Date','LeaveDeta')

class MoneySerializers(serializers.ModelSerializer):
    """消费金额"""
    #Room=serializers.CharField(source="Room.Room",read_only=True)
    #sm = models.Money.objects.aggregate(nums=Sum('Dmoney'))
    #Time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # 最后修改时间
    class Meta:
        model=models.Money
        #fields=('Dmoney','Lmoney','Room','Time')
        fields=('Dmoney','Lmoney')