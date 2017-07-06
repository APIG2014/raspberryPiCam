#!/usr/bin/env python

"""
starts the daemon to give remote acces to the raspery pi ressources.


Usage:
    run_camera_server.py [--port=<port>] [--IP=<IP>] [--allow_webcam] [--allow_picam]

    
Options:
    -h --help           show this screen.
    --port=<port>       port used to connect [default: 8000].
    --IP=<IP>           IP used by the daemon. default, will use interface that can reach 8.8.8.8
    --allow_webcam      allow the usage of the wecam [default: False].
    --allow_picam       allow the usage of the picam [default: False].
"""
from docopt import docopt

from raspberry_pi_cam.remotecamera.remotecameraserver import run_server
from raspberry_pi_cam.remotecamera.utils import get_my_ip





def main():
    arguments = docopt(__doc__)

    my_ip = arguments["--IP"]
    my_port = int(arguments["--port"])
    allow_webcam = arguments["--allow_webcam"]
    allow_webcam = True
    allow_picam = arguments["--allow_picam"]
    allow_picam = True

    if my_ip is None:
        print "no IP given, going to use interface that can reach 8.8.8.8"
        my_ip = get_my_ip()
        print "going to use: %s" % my_ip

    run_server(host=my_ip, port=my_port, allow_webcam=allow_webcam, allow_picam=allow_picam)


if __name__ == "__main__":
    main()

