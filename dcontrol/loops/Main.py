import gevent

from dcontrol.utils.loggingClass import LoggingClass


class MainLoop(LoggingClass):
    def __init__(self, que):
        super(MainLoop, self).__init__()
        self.que = que

    def event_loop(self):
        while True:
            e = self.que.Main.get()
            e.job_done()

    def run(self):
        return gevent.spawn(self.event_loop)
