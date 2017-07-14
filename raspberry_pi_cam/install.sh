#!/bin/bash

mkdir workspace
cd workspace


git clone https://github.com/APIG2014/raspberryPiCam.git raspberryPiCam



cd raspberryPiCam

# make the new package usable as developer mode
sudo ./setup develop



cd raspberry_pi_cam


# install the dependencies
sudo apt-get -y install python-docopt
sudo apt-get -y install python-opencv
sudo apt-get -y install python2-pyro4
sudo pip install serpent



sudo raspi-config
#    enable camera and I2c remote-GPIO



# to test:
./run_camera_server --help
    => print the help



# to start the camera server using the picam
./run_camera_server.py --allow_picam

# to start the camera client (using local camera server)
./run_one_camera_client.py


# to start the multi camera client
./run_multi_camera_client.py










