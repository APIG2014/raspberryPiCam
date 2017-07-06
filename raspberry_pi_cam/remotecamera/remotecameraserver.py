from __future__ import print_function
from remoteobject import RemoteObject
import Pyro4




def run_server(host="192.168.1.143", port=8000, allow_webcam=False, allow_picam=False):
    Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
    d = Pyro4.Daemon(host=host, port=port)
    uri = d.register(RemoteObject(allow_webcam=allow_webcam, allow_picam=allow_picam), "example.async")
    print("server object uri:",uri)
    print("async server running.")
    d.requestLoop()
