from gevent import monkey
monkey.patch_all()

import argparse

import logging
import gevent

from dcontrol.loops import MainLoop, ElgatoWS, DiscordIPC
from dcontrol.utils.que import Que

if __name__ == '__main__':
    logging.basicConfig(filename='dcontrol.log', level=logging.DEBUG)
    logging.info("Starting dev.nadie.dcontrol..")
    parser = argparse.ArgumentParser(description='Connect discord to streamdeck')
    parser.add_argument('-port', type=int, required=True, help='Port for steamdeck')
    parser.add_argument('-pluginUUID', type=str, required=True, help='UUID for plugin')
    parser.add_argument('-registerEvent', type=str, required=True, help='Event for plugin')
    parser.add_argument('-info', type=str, required=True, help='json info for plugin')
    args = parser.parse_args()

    que = Que()
    main_loop = MainLoop(que)
    ews = ElgatoWS(que, args.port, args.pluginUUID, args.registerEvent, args.info)
    dipc = DiscordIPC(que)
    gevent.joinall([main_loop.run(), ews.run(), dipc.run()], raise_error=True)

