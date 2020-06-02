class server_queue:
    def __init__(self,state,serverqueue):
        self.state=state
        self.serverqueue=serverqueue

    def is_full(self):
        return 0

    def in_queue(self,room_no):
        return 0

    def out_queue(self,room_no):
        return 0

    def if_in_sq(self,room_no):
        return 0