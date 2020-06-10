from air_condition_system import models
# class dispatch_queue():
#     def __init__(self,state,dispatchqueue):
#         self.state=state
#         self.dispatchqueue=dispatchqueue
#
# def in_queue(room_no):#把对应的房间号加入到server_queue_db数据库中，并把对应从控机的状态修改为start_up，并打开相应的计时器
#     sq = models.server_queue_db()
#     sq.room_no = room_no
#     sq.save()
#     models.sub_controller_db.objects.filter(room_no=room_no).update(is_start_up=True)
#     return 0
def in_queue(room_no):
    dq = models.dispatch_queue_db()
    dq.room_no = room_no
    dq.save()
    models.sub_controller_db.objects.filter(room_no=room_no).update(dur_time=0)
    return 0

def out_queue(room_no):
    models.dispatch_queue_db.objects.filter(room_no=room_no).delete()
    return 0

def if_empty():
    dq = models.dispatch_queue_db.objects.all()
    if dq.count() == 0:
        return True
    else:
        return False