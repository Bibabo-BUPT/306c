from django.db import models
from django.utils import timezone
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
    is_out_queue = models.BooleanField(default=True)#是否在等待队列和服务队列之外（即室温达到了目标温度之后触发的状态）
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
    dur_time=models.IntegerField(default=0)#计时器，用来记录当前机器的等待或被服务的时长
    cur_rate=models.FloatField(default=0)#当前费率，和风速保持一致
    top_temp = models.IntegerField(default=0)#最高温度
    bottom_temp = models.IntegerField(default=0)#最低温度

class server_queue_db(models.Model):
    room_no = models.IntegerField(default=0)

class dispatch_queue_db(models.Model):
    room_no = models.IntegerField(default=0)


class User(models.Model):
    """用户"""
    Room = models.CharField(verbose_name="房间号", max_length=10)
    Entry = models.DateTimeField(verbose_name="入驻时间", auto_now=True)
    Leave = models.DateTimeField(verbose_name="离开时间", auto_now=True)
    Time = models.DateTimeField(verbose_name="订单创建时间", default=timezone.now)

    class Meta:
        verbose_name_plural = "用户"

    def __str__(self):
        return self.Name


class Record(models.Model):
    """记录表"""
    #Room = models.ForeignKey(User, help_text='房间号', on_delete=models.CASCADE, null=False)
    Room = models.IntegerField(verbose_name="房间号")
    #DeDu = models.IntegerField(verbose_name="室温温度")#这里他本来写的默认值，之后改成室温了，这个值暂时先不用了，直接在前端算吧
    DangDu = models.IntegerField(verbose_name="当前温度")#指的是当前的目标温度
    Pattern = models.CharField(verbose_name="模式", default="制冷", max_length=10)
    Speed = models.CharField(verbose_name="风速", max_length=10, default=1)  # 风速分为1 23个 档位
    State = models.CharField(verbose_name="当前状态", max_length=10, default="关机")  # 默认关机状态
    #以下三个值我之后需要改一下，只留记录的开始时间和结束时间就可以了
    StartDate = models.DateTimeField(verbose_name="开机时间", default=timezone.now)
    Date = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)
    LeaveDate = models.DateTimeField(verbose_name="关机时间", default=timezone.now)
    cost = models.FloatField(default=0)#本次服务的花费
    feerate = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "记录表"

    def __str__(self):
        return self.State


class Money(models.Model):
    """记录金额"""
    Lmoney = models.FloatField(verbose_name="累计金额", max_length=100)
    Room = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "金额"

class count(models.Model):
    dispatch_time = models.IntegerField(default=0)#被调度次数
    open_time = models.IntegerField(default=0)#空调开关次数，开+关算一次
    change_temper_time = models.IntegerField(default=0)#改变温度的次数
    change_speed_time = models.IntegerField(default=0)#改变风速的次数
    room_id = models.IntegerField(default=0)
