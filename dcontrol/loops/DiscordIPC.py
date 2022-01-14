import gevent.event

from dcontrol.utils.loggingClass import LoggingClass


class DiscordIPC(LoggingClass):
    def __init__(self, que):
        super(DiscordIPC, self).__init__()
        self.que = que

    def connect_and_run(self):
        pass

    def run(self):
        return gevent.spawn(self.connect_and_run)
