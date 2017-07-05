import sys
import time
import Pyro4


def get_remote_object(host="192.168.1.143", port=8000):
    try:
        print Pyro4.config.SERIALIZERS_ACCEPTED
        Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
        print Pyro4.config.SERIALIZERS_ACCEPTED

        Pyro4.config.SERIALIZER = 'pickle'
        uri="PYRO:example.async@" + host + ":" + str(port)
        proxy = Pyro4.Proxy(uri)

    except:
        print "something bad happend we can't continue"
        raise

    return proxy