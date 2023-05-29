class Event(object):
    def __init__(self):
        self.is_canceled = False

    def cancel(self):
        self.is_canceled = True
