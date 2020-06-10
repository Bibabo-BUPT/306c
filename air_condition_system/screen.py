class screen:
    def __init__(self,target_temper,temper,speed,mode,current_fee,total_fee,room_no,state):
        self.target_temper=target_temper
        self.temper=temper
        self.speed=speed
        self.mode=mode
        self.current_fee=current_fee
        self.total_fee=total_fee
        self.room_no=room_no
        self.state=state

    def create(self):
        return 0

    def show_running_state(self,room_no):
        return 0

    def delete(self):
        return 0
