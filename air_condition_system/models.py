from django.db import models

# Create your models here.
class room_db(models.Model):
    room_no=models.IntegerField(default=0)
    temper=models.FloatField(default=0)
    customer=models.IntegerField(default=0)

class detailed_list_room_db(models.Model):
    date=models.CharField(max_length=50,null=True)
    time=models.CharField(max_length=50,null=True)
    room_no=models.IntegerField(default=0)
    total_fee=models.FloatField(default=0)
    target_temper=models.FloatField(default=0)
    speed=models.IntegerField(default=0)

class main_controller_db(models.Model):
    """"
    main_controller的每一条记录代表着一次开关机，因为不同开关机的设置可能不同，可以根据主控机的状态判断当前正在运行的
    （但实际上在验收环境中我们只可能产生一条主控机记录）
    因此本设计只是为了系统的可扩展性，在验收时并未使用到
    """
    default_mode = models.IntegerField(default=0)
    default_temper = models.IntegerField(default=0)
    default_speed = models.IntegerField(default=0)
    feerateL = models.FloatField(default=0)
    feerateM = models.FloatField(default=0)
    feerateH = models.FloatField(default=0)
    state = models.IntegerField(default=-1)#设置模式为0，工作模式为1
    room_num = models.IntegerField(default=0)
    allow_num = models.IntegerField(default=0)


class sub_controller_db(models.Model):
    is_check_in=models.BooleanField(default=False)#房间是否入住
    is_power_on=models.BooleanField(default=False)#空调是否开机
    is_start_up=models.BooleanField(default=False)#空调是否在服务中
    mode=models.IntegerField(default=0)#0为制冷模式，1为制热模式
    speed=models.IntegerField(default=0)#0为低速，1为中速，2为高速
    target_temper=models.FloatField(default=0)
    current_fee=models.FloatField(default=0)
    total_fee=models.FloatField(default=0)
    room_no=models.IntegerField(default=0,primary_key=True)
    temper=models.FloatField(default=0)
    feerateL = models.FloatField(default=0)
    feerateM = models.FloatField(default=0)
    feerateH = models.FloatField(default=0)
    default_mode = models.IntegerField(default=0)
    default_temper = models.IntegerField(default=0)
    default_speed = models.IntegerField(default=0)
    dur_time=models.FloatField(default=0)#计时器，用来记录当前机器的等待或被服务的时长
    cur_rate=models.FloatField(default=0)#当前费率，和风速保持一致

class server_queue_db(models.Model):
    room_no = models.ForeignKey('sub_controller_db',on_delete=models.CASCADE)

class dispatch_queue_db(models.Model):
    room_no = models.ForeignKey('sub_controller_db',on_delete=models.CASCADE)