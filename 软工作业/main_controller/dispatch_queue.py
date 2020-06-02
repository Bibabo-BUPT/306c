class dispatch_queue():
    def __init__(self,state,dispatchqueue):
        self.state=state
        self.dispatchqueue=dispatchqueue

    def in_queue(self,room_no):
        return 0

    def out_queue(self,room_no):
        return 0

    def if_empty(self):
        return 0