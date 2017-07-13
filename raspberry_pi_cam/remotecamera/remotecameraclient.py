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
    def __init__(self, use_async=True):
        self.IPs = []
        self.remote_cameras = []
        self.use_async = use_async
        self.async_called = False
        self.async_frames = []

    def add_camera(self, IP, port):
        self.IPs.append(IP+str(port))
        if self.use_async:
            remote_camera = Pyro4.async(get_remote_object(host=IP, port=port))
        else:
            remote_camera = get_remote_object(host=IP, port=port)

        self.remote_cameras.append(remote_camera)

    def cameras_start(self):
        return_val = True
        if self.use_async:
            async_vals =[]
            for camera in self.remote_cameras:
                async_vals.append(camera.camera_start(resolution=(640, 480)))

            for async_val in async_vals:
                print type(async_val.value)
                return_val &= async_val.value
        else:
            for camera in self.remote_cameras:
                return_val &= camera.camera_start(resolution=(640, 480))
        return return_val

    def cameras_get_frame(self):


        ret_frame = []

        if self.use_async:

            if self.async_called is False:
                self.camera_get_frame_async()

            for async_frame in self.async_frames:
                ret_frame.append(async_frame.value)
            self.async_called = False

        else:
            for camera in self.remote_cameras:
                ret_frame.append( camera.camera_get_frame())



        return ret_frame


    def camera_get_frame_async(self):
        if self.use_async is True:
            del self.async_frames[:]

            for camera in self.remote_cameras:
                self.async_frames.append(camera.camera_get_frame())
            self.async_called = True