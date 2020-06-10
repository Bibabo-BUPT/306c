from air_condition_system import models
# class main_controller():
#     def __init__(self,default_mode,default_temper,default_speed,feerateL,feerateM,feerateH):
#         self.default_mode=default_mode
#         self.default_temper=default_temper
#         self.default_speed=default_speed
#         self.feerateL=feerateL
#         self.feerateM=feerateM
#         self.feerateH=feerateH

def calculate_current_fee(self,room_no,time):
    return 0

def calculate_total_fee(selfself,room,time):
    return 0

def set_default_temper(self,temper):
    return 0

def set_default_mode(self,mode):
    return 0

def set_default_speed(self,speed):
    return 0

def set_accounting_rule(self,low,mid,high):
    return 0

def ispoweroff(self):
    return 0

def set_default(mode,speed,default_temper,feerateL,feerateM,feerateH,state,room_num,allow_num):
    mc = models.main_controller_db.objects.get(id=1)
    mc.default_mode = mode
    mc.default_temper = default_temper
    mc.default_speed = speed
    mc.feerateL = feerateL
    mc.feerateM = feerateM
    mc.feerateH = feerateH
    mc.state = state
    mc.room_num = room_num
    mc.allow_num = allow_num
    mc.save()

