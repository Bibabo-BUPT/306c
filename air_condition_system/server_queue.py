from air_condition_system import models


# class server_queue:
#     def __init__(self,state,serverqueue):
#         self.state=state
#         self.serverqueue=serverqueue

def is_full(allow_num):
    sq = models.server_queue_db.objects.all()
    num = sq.count()
    if num < allow_num:
        return True
    else:
        return False


def in_queue(room_no):  # 把对应的房间号加入到server_queue_db数据库中，并把对应从控机的状态修改为start_up，并打开相应的计时器
    sq = models.server_queue_db()
    sq.room_no = room_no
    sq.save()
    models.sub_controller_db.objects.filter(room_no=room_no).update(is_start_up=True)
    models.sub_controller_db.objects.filter(room_no=room_no).update(dur_time=0)
    last_dis_time = models.count.objects.filter(room_id=room_no).first().dispatch_time
    models.count.objects.filter(room_id=room_no).update(dispatch_time=last_dis_time + 1)
    return 0


def out_queue(room_no):  # 把对应的房间号加入到dispatch_queue_db数据库中，并把对应从控机的状态的start_up修改，关闭相应的计时器
    models.server_queue_db.objects.filter(room_no=room_no).delete()
    models.sub_controller_db.objects.filter(room_no=room_no).update(is_start_up=False)
    return 0


def if_in_sq(room_no):  # 遍历整个sq，查找对应的房间号是否在里面
    sq = models.server_queue_db.objects.filter(room_no=room_no)
    if sq.count() == 0:
        return False
    else:
        print("in here")
        return True
