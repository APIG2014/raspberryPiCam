#!/usr/bin/env python

"""
starts the daemon to give remote acces to the raspery pi ressources.


Usage:
    run_camera_server.py [--port=<port>] [--IP=<IP>] [--use_picam|--use_webcam]

Options:
    -h --help           show this screen.
    --port=<port>       port used to connect [default: 8000].
    --IP=<IP>           IP used by the daemon. default, will use interface that can reach 8.8.8.8
    --use_picam         use the picamera
    --use_webcam         use the webcam


"""
from docopt import docopt

from raspberry_pi_cam.remotecamera.remotecameraclient import get_remote_object
from raspberry_pi_cam.remotecamera.utils import get_my_ip, signal_handler_ctrlc
import cv2
import signal





def main():

    arguments = docopt(__doc__)
    print arguments
    
    my_ip = arguments["--IP"]
    my_port = arguments["--port"]
    use_picam = arguments["--use_picam"]

    if my_ip is None:
        print "no IP given, going to use interface that can reach 8.8.8.8"
        my_ip = get_my_ip()
        print "going to use: %s" % my_ip

    remote_camera = get_remote_object(host=my_ip, port=my_port)

    signal.signal(signal.SIGINT, signal_handler_ctrlc)

    if use_picam:
        is_camera_built = remote_camera.picam_start()
        if is_camera_built is False:
            print "the server doesn't suport picam"
            exit(0)
        else:
            print "the server is up an running with our picam"
    else:
        is_camera_built = remote_camera.webcam_start()
        if is_camera_built is False:
            print "the server doesn't suport webcam"
            exit(0)
        else:
            print "the server is up an running with our webcam"

    while True:
        if use_picam:
            remote_frame = remote_camera.picam_get_frame()
        else:
            remote_frame = remote_camera.webcam_get_frame()
        cv2.imshow("preview", remote_frame.frame)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break



    cv2.destroyWindow("preview")
if __name__ == "__main__":
    main()

