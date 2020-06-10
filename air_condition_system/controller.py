from air_condition_system import models
import os,django
import server_queue
import dispatch_queue
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controller.settings")# project_name 项目名称
django.setup()

from django.db import connection

def power_on(room_no):
    #首先判断服务队列是否是满的，若有空，则可以直接进队列

    mc = models.main_controller_db.objects.filter(id=1)
    default_speed = mc[0].default_speed#获得空调的默认风速
    # 找到所有的服务队列中的机器，并按照speed值升序排序,其次按照服务时间降序排序，最后再sc中排位最靠前的机器，越应该被出队列
    sc = models.sub_controller_db.objects.filter(is_start_up=True).order_by("speed","-dur_time")
    """
    接下来对比sc中第一个的风速，若小于默认风速，则直接把第一个换下来，
    若等于默认风速，则比较是否大于120s，若大于，则将其替换出来，若不大于，则把该空调放进等待队列；
    若大于默认风俗，则该空调直接进等待队列
    """
    if sc[0].speed < default_speed:
        server_queue.out_queue(sc[0].room_no)
        server_queue.in_queue(room_no)
        dispatch_queue.in_queue((sc[0].room_no))
    elif sc[0].speed > default_speed:
        dispatch_queue.in_queue(room_no)
    else:
        if sc[0].dur_time >= 120:
            server_queue.out_queue(sc[0].room_no)
            server_queue.in_queue(room_no)
            dispatch_queue.in_queue((sc[0].room_no))
        else:
            dispatch_queue.in_queue(room_no)

def temper_change(room_no,temper):

    return 0

def change_target_temper(self,room_no,target_temper):
    return 0

def change_speed(self,room_no,speed):
    return 0

def show_fee(self,room_no,time):
    return 0

def power_off(room_no,time):#从控机关机
    is_in_sq=server_queue.if_in_sq()
    if_dq_empty=dispatch_queue.if_empty()
    if is_in_sq == True and if_dq_empty == False:#如果这个机器在服务队列里,且调度队列不为空
        #把等待队列按照风速递减，等待时间递减排队，此时等待队列中的第一个就是应该进入调度队列的
        dq = models.sub_controller_db.objects.filter(is_power_on=True).filter(is_start_up=False).order_by("-speed","-dur_time")
        dispatch_queue.out_queue(room_no)
        server_queue.in_queue(room_no)
    server_queue.out_queue(room_no)
    return 0

def print_bill(self,room_no):
    return 0

def print_daily_record(self,room_no,record_type):
    return 0

def print_weekly_record(self, room_no, record_type):
    return 0

def set_default_temper(self,default_temper):
    return 0

def set_default_mode(self,default_mode):
    return 0

def set_default_speed(self,default_speed):
    return 0

def set_accounting_rule(self,low,mid,high):
    return 0

def find_ac(self,room_no):
    return 0

def power_off_mc(self):#主控机关机
    return 0

def create_sq(self):
    return 0

def create_dq(self):
    return 0

def create_dr(self):
    return 0

def create_wr(self):
    return 0

def create_bill(self):
    return 0

def create_detaild_record(self):
    return 0
