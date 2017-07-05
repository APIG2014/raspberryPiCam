from __future__ import print_function
import time
import cv2
import time




class RemoteFrame(object):
    def __init__(self):
        pass



class RemoteObject(object):
    def __init__(self, allow_webcam=False):
        self._camera_set_up = False


        #webcam stuff
        self.allow_webcam = allow_webcam
        self.webcam = None
        if self.allow_webcam:
            print("webcam allowed for this server")

        print("remote object built")

    @property
    def camera_set_up(self):
        return self._camera_set_up

    @camera_set_up.setter
    def camera_set_up(self, value):
        self._camera_set_up = value

    def webcam_start(self):
        if self.allow_webcam:
            self.webcam = cv2.VideoCapture(0)

            if self.webcam.isOpened():  # try to get the first frame
                rval, frame = self.webcam.read()
            else:
                rval = False
        else:
            rval = False
        return rval

    def webcam_get_frame(self):
        ret_frame = RemoteFrame()
        rval, frame = self.webcam.read()
        ret_frame.frame = frame

        return ret_frame

    def divide(self, a, b):
        print("dividing {0} by {1} after a slight delay".format(a, b))
        time.sleep(3)
        return a // b

    def multiply(self, a, b):
        print("multiply {0} by {1}, no delay".format(a, b))
        return a * b

    def add(self, value, increase):
        print("adding {1} to {0}, no delay".format(value, increase))
        return value + increase