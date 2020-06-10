class detailed_list_customer:
    def __init__(self,date,time,room_no,total_fee,target_temper,speed,customer):
        self.date=date
        self.time=time
        self.room_no=room_no
        self.total_fee=total_fee
        self.target_temper=target_temper
        self.speed=speed
        self.customer=customer

    def calculate(self):
        return 0