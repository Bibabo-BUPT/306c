class detailed_record:
    def __init__(self,detail_count,room_no,request_time,duration,temper,speed,fee):
        self.detail_count = detail_count  # 详单编号
        self.room_no=room_no #房间号
        self.request_time=request_time #请求时间
        self.duration=duration #请求持续时间
        self.temper=temper #温度
        self.speed=speed #风速
        self.fee=fee #期间费用

    def print_detail_record(self,room_no):
        return 0