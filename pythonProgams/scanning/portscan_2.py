#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2) #timeout after 2s

host = input("[*] enter the host to scan  :");

def portscanner(port):
    if sock.connect_ex((host, port)):
        print ("Port %d is closed" % (port))
    else:
        print ("Port %d is open" % (port))

for port in range(1,100):
    portscanner(port)
