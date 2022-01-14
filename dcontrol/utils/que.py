import gevent.queue


class Que:
    def __init__(self):
        self.Main = gevent.queue.Queue()
        self.Elgato = gevent.queue.Queue()
