# Control discord w/ streamdeck
__**Good Morning!**__

This is my attempt of making a Streamdeck plugin to interface with the streamdeck sdk and Discord IPC sdk with Python

# Warning:
I would not recomend using this nor is it recomended to use python with streamdeck Even though im packing it with cx_freeze but hey it gives me **_serotonin_** so fuck it.

## What/how it should work:
* Yes I'm using *Gevent* I don't care about AsyncIO as much as the implmentation is better, I rather and used to gevent with BetterDisco :)
* This mainly using a gevent que system to talk between the 3 greenlet threads `gevent.queue.Queue()`
* The Socket to Elgato I'm just using a monkey patched Websocket-client instance
* For Discord I'm thinking of using the native IPC supported my discord. 
  * I was origionaly thinking of using the websocket thats listening on localhost but thats not available :(
