#!/usr/bin/env python

"""
starts the daemon to give remote acces to the raspery pi ressources.


Usage:
    run_camera_server.py [--IP0=<IP>] [--IP1=<IP>] [--IP2=<IP>] [--IP3=<IP>]

Options:
    -h --help           show this screen.
    --IP0=<IP>           IP used by the daemon. default, will use interface that can reach 8.8.8.8
    --IP1=<IP>           IP used by the daemon. default, no use of this remote camera
    --IP2=<IP>           IP used by the daemon. default, no use of this remote camera
    --IP3=<IP>           IP used by the daemon. default, no use of this remote camera



"""
from docopt import docopt

from raspberry_pi_cam.remotecamera.remotecameraclient import MultiCameraClient
from raspberry_pi_cam.remotecamera.utils import get_my_ip
import cv2





def main():

    arguments = docopt(__doc__)
    print arguments

    remote_ip0 = arguments["--IP0"]
    remote_ip1 = arguments["--IP1"]
    remote_ip2 = arguments["--IP2"]
    remote_ip3 = arguments["--IP3"]
    remote_port = 8000




    if remote_ip0 is None:
        print "no IP given, going to use interface that can reach 8.8.8.8"
        remote_ip0 = get_my_ip()
        print "going to use: %s" % remote_ip0



    multi_camera = MultiCameraClient(use_async=False)

    if remote_ip0 is not None:
        multi_camera.add_camera(remote_ip0, remote_port)
    if remote_ip1 is not None:
        multi_camera.add_camera(remote_ip1, remote_port)
    if remote_ip2 is not None:
        multi_camera.add_camera(remote_ip2, remote_port)
    if remote_ip3 is not None:
        multi_camera.add_camera(remote_ip3, remote_port)

    multi_camera.cameras_start()

    while True:
        frames = multi_camera.cameras_get_frame()
        id = 0
        for frame in frames:
            cv2.imshow("preview" + str(id), frame.frame)
            id += 1

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break



    cv2.destroyWindow("preview")
if __name__ == "__main__":
    main()

