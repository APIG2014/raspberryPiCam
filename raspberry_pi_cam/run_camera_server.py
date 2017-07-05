
"""
starts the daemon to give remote acces to the raspery pi ressources.


Usage:
    run_camera_server.py 
    
    
Options:
    -h --help           show this screen


"""
from docopt import docopt

from raspberry_pi_cam.remotecamera.remotecameraserver import run_server





def main():
    arguments = docopt(__doc__)

    run_server(host="192.168.1.143", port=8000)


if __name__ == "__main__":
    main()

