from django.http import HttpResponse
from django.shortcuts import render, redirect
from air_condition_system import models
def timer_begin(room_no):
    return 0

def get_timer(room_no):
    return 0

def timer_end(room_no):
    return 0

def compare(sroom_no,temper):
    return 0
def set_state_on(room_no,temper):
    return 0

def get_default_mode():
    return 0

def alter_target_temper(mode,room_no):#修改数据库中的温度值
    #这个传入的mode实际上指的是新的温度，而非模式
    sc = models.sub_controller_db.objects.filter(room_no=room_no)
    sc.update(target_temper=mode)
    return 0

def alter_speed(mode,room_no):
    # 这个传入的mode实际上指的是新的风速，而非模式
    sc = models.sub_controller_db.objects.filter(room_no=room_no)
    sc.update(speed=mode)
    return 0

def power_off(room_no,time):
    return 0

def set_default_temper(default_temper):
    return 0

def set_default_mode(default_mode):
    return 0

def set_default_speed(default_speed):
    return 0

def query_running_state():
    return 0

def ispoweroff():
    return 0

def set_default(mode,speed,default_temper,feerateL,feerateM,feerateH):
    for room_no in range(601, 606):
        res = models.sub_controller_db.objects.filter(room_no=room_no)
        res2 = models.count.objects.filter(room_id=room_no)
        res3 = models.Money.objects.filter(Room=room_no)
        if res.count() == 0:#如果数据库中暂无该房间的记录：
            sc = models.sub_controller_db()
        else:
            sc = models.sub_controller_db.objects.filter(room_no=room_no)[0]
        sc.room_no = room_no
        sc.is_check_in = False
        sc.is_power_on = False
        sc.is_start_up = False
        sc.is_out_queue = True
        sc.mode = mode
        sc.speed = speed
        sc.target_temper = default_temper
        sc.current_fee = 0
        sc.total_fee = 0
        sc.temper = 0
        sc.feerateL = feerateL
        sc.feerateM = feerateM
        sc.feerateH = feerateH
        sc.default_mode = mode
        sc.default_temper = default_temper
        sc.default_speed = speed
        sc.dur_time = 0
        if sc.speed == 0:
            sc.cur_rate = feerateL
        elif sc.speed == 1:
            sc.cur_rate = feerateM
        else:
            sc.cur_rate = feerateH
        if sc.mode == 0:#0是冷模式
            sc.top_temp=25
            sc.bottom_temp=18
        else:#1是暖模式
            sc.top_temp=30
            sc.bottom_temp=25

        sc.save()


        if res2.count() == 0:
            cu = models.count()
        else:
            cu = models.count.objects.filter(room_id=room_no)[0]
        cu.open_time = 0
        cu.dispatch_time = 0
        cu.change_temper_time = 0
        cu.change_speed_time = 0
        cu.room_id = room_no

        cu.save()

        if res3.count() == 0:
            mn = models.Money()
        else:
            mn = models.Money.objects.filter(Room=room_no)[0]
        mn.Room = room_no
        mn.Lmoney = 0

        mn.save()

    return 0


