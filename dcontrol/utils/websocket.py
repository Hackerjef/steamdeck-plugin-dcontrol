import websocket

from dcontrol.utils.loggingClass import LoggingClass


class Websocket(LoggingClass, websocket.WebSocketApp):
    def __init__(self, *args, **kwargs):
        LoggingClass.__init__(self)
        websocket.enableTrace(True)
        websocket.WebSocketApp.__init__(self, *args, **kwargs)
