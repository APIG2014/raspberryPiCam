#!/usr/bin/env python

"""
starts the daemon to give remote acces to the raspery pi ressources.


Usage:
    run_camera_server.py [--port=<port>] [--IP=<IP>]

Options:
    -h --help           show this screen.
    --port=<port>       port used to connect [default: 8000].
    --IP=<IP>           IP used by the daemon. default, will use interface that can reach 8.8.8.8

"""
from docopt import docopt

from raspberry_pi_cam.remotecamera.remotecameraclient import get_remote_object
from raspberry_pi_cam.remotecamera.utils import get_my_ip
import cv2



def main():
    arguments = docopt(__doc__)

    my_ip = arguments["--IP"]
    my_port = arguments["--port"]

    if my_ip is None:
        print "no IP given, going to use interface that can reach 8.8.8.8"
        my_ip = get_my_ip()
        print "going to use: %s" % my_ip

    remote_camera = get_remote_object(host=my_ip, port=8000)
    remote_camera.webcam_start()

    while True:
        remote_frame = remote_camera.webcam_get_frame()
        cv2.imshow("preview", remote_frame.frame)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break



    cv2.destroyWindow("preview")
if __name__ == "__main__":
    main()

