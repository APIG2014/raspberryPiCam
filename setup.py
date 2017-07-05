#!/usr/bin/env python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

REQUIREMENTS = ['Pyro4==4.23', 'docopt', 'setuptools']


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "raspberryPiCam",
    version = "0.0.1",
    author = "Albena Iotova-gagnaire",
    author_email = "",
    description = (""),
    license = "GNU",
    keywords = "",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['raspberry_pi_cam'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires = REQUIREMENTS,
)
