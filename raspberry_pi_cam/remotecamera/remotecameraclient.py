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


class MultiCameraClient(object):
    def __init__(self):
        self.IPs = []
        self.remote_cameras = []

    def add_camera(self, IP, port):
        self.IPs.append(IP+str(port))
        self.remote_cameras.append( get_remote_object(host=IP, port=port))

    def cameras_start(self):
        for camera in self.remote_cameras:
            camera.camera_start()

    def cameras_get_frame(self):
        ret_frame = []
        for camera in self.remote_cameras:
            ret_frame.append( camera.camera_get_frame() )
        return ret_frame