from django.http import HttpResponse
from django.shortcuts import render, redirect
from main_controller import models
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

def alter_target_temper(mode):
    return 0

def alter_speed(mode):
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
    for room_no in range(1, 6):
        sc = models.sub_controller_db()
        sc.room_no = room_no + 600
        sc.is_check_in = False
        sc.is_power_on = False
        sc.is_start_up = False
        sc.mode = mode
        sc.speed = speed
        sc.target_temper = default_temper
        sc.current_fee = 0
        sc.total_fee = 0
        sc.room_no = room_no + 600
        sc.temper = 0
        sc.feerateL = feerateL
        sc.feerateM = feerateM
        sc.feerateH = feerateH
        sc.default_mode = mode
        sc.default_temper = default_temper
        sc.default_speed = speed
        sc.dur_time = 0
        if sc.mode == 0:
            sc.cur_rate = feerateL
        elif sc.mode == 1:
            sc.cur_rate = feerateM
        else:
            sc.cur_rate = feerateH
        sc.save()
    return 0


