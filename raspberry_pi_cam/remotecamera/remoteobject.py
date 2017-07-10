from __future__ import print_function
import time
import cv2
import time
import io
import numpy

class RemoteFrame(object):
    def __init__(self):
        pass



class RemoteObject(object):
    def __init__(self, allow_webcam=False, allow_picam=False):
        self._camera_set_up = False


        #webcam stuff
        self.allow_webcam = allow_webcam
        self.webcam = None
        if self.allow_webcam:
            print("webcam allowed for this server")

        #picam stuff
        self.allow_picam = allow_picam
        self.picam = None
        self.picam_stream = None
        if self.allow_picam:
            print("picam allowed for this server")
        
            
            
        print("remote object built")

    @property
    def camera_set_up(self):
        return self._camera_set_up

    @camera_set_up.setter
    def camera_set_up(self, value):
        self._camera_set_up = value

    def webcam_start(self):
        if self.allow_webcam:
            if self.webcam is None:
                self.webcam = cv2.VideoCapture(0)
            else:
                # we already created the object, let's use it!
                pass

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

    
    #function for starting pi camera
    def picam_start(self):
        if self.allow_picam:
            import picamera
            self.picam = picamera.PiCamera()
                        
            self.picam_stream = io.BytesIO() 
          
            self.picam.capture(self.picam_stream, format='jpeg', use_video_port=True)
            # Construct a numpy array from the stream
            data = numpy.fromstring(self.picam_stream.getvalue(), dtype=numpy.uint8)
            # "Decode" the image from the array, preserving colour
            image = cv2.imdecode(data, 1)
            #clear buffer
            self.picam_stream.seek(0)
            rval = True
        else:
            rval = False
        print ("end of picam_start function")
        return rval

    def picam_get_frame(self):
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
