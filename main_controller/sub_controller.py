class sub_controller:
    def __init__(self,state,mode,speed,target_temper,current_fee,total_fee,room_no):
        self.state=state
        self.mode=mode
        self.speed=speed
        self.target_temper=target_temper
        self.current_fee=current_fee
        self.total_fee=total_fee
        self.room_no=room_no

    def timer_begin(self,room_no):
        return 0

    def get_timer(selfroom_no):
        return 0

    def timer_end(selfroom_no):
        return 0

    def compare(self,room_no,temper):
        return 0
    def set_state_on(self,room_no,temper):
        return 0

    def get_default_mode(self):
        return 0

    def alter_target_temper(self,mode):
        return 0

    def alter_speed(selfmode):
        return 0

    def power_off(self,room_no,time):
        return 0

    def set_default_temper(self,default_temper):
        return 0

    def set_default_mode(self,default_mode):
        return 0

    def set_default_speed(self,default_speed):
        return 0

    def query_running_state(self):
        return 0

    def ispoweroff(self):
        return 0
