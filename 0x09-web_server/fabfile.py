#!/usr/bin/python3

from fabric.api import *

def pack():

def deploy():
    sudo("mkdir /tmp/holbertonwebapp")
    sudo
    put(local_path="./holbertonwebapp.tar.gz", remote_path="/tmp/holbertonwebapp/holbertonwebapp.tar.gz")

def clean():
