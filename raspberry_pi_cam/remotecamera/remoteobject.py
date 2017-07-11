#from __future__ import print_function
import time
import cv2
import time
import io
import numpy

class RemoteFrame(object):
    def __init__(self):
        self.frame = None



class RemoteObject(object):
    def __init__(self, allow_webcam=False, allow_picam=False):

        #webcam stuff
        self._allow_webcam = allow_webcam
        self.webcam = None
        if self._allow_webcam is True:
            print "webcam allowed for this server"

        #picam stuff
        self._allow_picam = allow_picam
        self.picam = None
        self.picam_stream = None
        if self._allow_picam is True:
            print "picam allowed for this server"
        
            
            
        print "remote object built"





    def allow_webcam(self):
        return self._allow_webcam
    def allow_picam(self):
        return self._allow_picam

    def webcam_start(self):
        if self._allow_webcam:
            if self.webcam is None:
                self.webcam = cv2.VideoCapture(0)
            else:
                # we already created the object, let's use it!
                pass

            if self.webcam.isOpened():  # try to get the first frame
                rval, frame = self.webcam.read()
                print "first images shape:", frame.shape
            else:
                rval = False
        else:
            rval = False
        return rval
 
    def webcam_get_frame(self):
        if self._allow_webcam:
            ret_frame = RemoteFrame()
            rval, frame = self.webcam.read()
            ret_frame.frame = frame

            return ret_frame
        else:
            # this server doesn't allow webcam
            return None
    
    #function for starting pi camera
    def picam_start(self, resolution=(480, 640)):
        if self._allow_picam:
            import picamera
            if self.picam is None:
                self.picam = picamera.PiCamera()
                self.picam_stream = io.BytesIO()
            else:
                # we already have a picam open, use that one
                pass

            self.picam.resolution = resolution

            self.picam.capture(self.picam_stream, format='jpeg', use_video_port=True)
            # Construct a numpy array from the stream
            data = numpy.fromstring(self.picam_stream.getvalue(), dtype=numpy.uint8)
            # "Decode" the image from the array, preserving colour
            image = cv2.imdecode(data, 1)
            #clear buffer
            self.picam_stream.seek(0)
            print "first images shape:", image.shape
            rval = True
        else:
            rval = False
        return rval

    def picam_get_frame(self):
        if self._allow_picam:
            ret_frame = RemoteFrame()
            self.picam.capture(self.picam_stream, format='jpeg', use_video_port=True)
            # Construct a numpy array from the stream
            data = numpy.fromstring(self.picam_stream.getvalue(), dtype=numpy.uint8)
            # "Decode" the image from the array, preserving colour
            image = cv2.imdecode(data, 1)
            #clear buffer
            self.picam_stream.seek(0)

            ret_frame.frame = image

            return ret_frame
        else:
            # this server doesn't allow the picam
            return None


    def divide(self, a, b):
        #print("dividing {0} by {1} after a slight delay".format(a, b))
        time.sleep(3)
        return a // b

    def multiply(self, a, b):
        #print("multiply {0} by {1}, no delay".format(a, b))
        return a * b

    def add(self, value, increase):
        #print("adding {1} to {0}, no delay".format(value, increase))
        return value + increase



    def camera_start(self, resolution=(480, 640)):
        if self._allow_picam:
            return self.picam_start(resolution=resolution)
        elif self._allow_webcam:
            return self.webcam_start()
        else:
            return False

    def camera_get_frame(self):
        if self._allow_picam:
            return self.picam_get_frame()
        elif self._allow_webcam:
            return self.webcam_get_frame()
        else:
            return False