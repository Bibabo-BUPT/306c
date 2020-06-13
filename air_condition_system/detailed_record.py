class detailed_record:
    def __init__(self,room_id,speed,rate,start_time,end_time,dur_cost):
        self.room_id = room_id  # 房间号
        self.speed=speed #速度
        self.rate=rate #费率
        self.start_time=start_time #开始时间
        self.end_time=end_time #结束时间
        self.dur_cost=dur_cost #期间费用

    def print_detail_record(self,room_no):
        return 0