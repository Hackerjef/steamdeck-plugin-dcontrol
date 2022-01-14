import json
import gevent.event

from dcontrol.utils.loggingClass import LoggingClass
from dcontrol.utils.websocket import Websocket


class ElgatoWS(LoggingClass):
    def __init__(self, que, port, pluginUUID, registerEvent, info):
        super(ElgatoWS, self).__init__()
        self.que = que
        self.port = port
        self.pluginUUID = pluginUUID
        self.registerEvent = registerEvent
        self.info = json.loads(info)
        self.ws = None
        self.ws_event = gevent.event.Event()

    def on_message(self, ws, message):
        pass

    def on_error(self, ws, error):
        self.log.error(error)

    def on_close(self, ws, close_status_code, close_msg):
        self.log.info(f'Websocket closed for Elgato')

    # run when websocket is initialised
    def on_open(self, ws):
        ws.send(json.dumps({"event": self.registerEvent, "uuid": self.pluginUUID}))
        self.log.info(f'Connected to Elgato')

    def connect_and_run(self):
        self.ws = Websocket(url=f"ws://localhost:{self.port}", on_error=self.on_error, on_close=self.on_close, on_open=self.on_open)
        self.ws.run_forever()
        self.ws_event.wait()

    def run(self):
        return gevent.spawn(self.connect_and_run)
