from air_condition_system import models
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