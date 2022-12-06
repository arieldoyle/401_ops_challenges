#!/usr/bin/python3
 
# Script: Ops 401 Class 44 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 05DEC2022      
# Purpose: 
       
# Resources:
    # https://docs.python.org/3/library/socket.html
    # https://www.kite.com/python/answers/how-to-check-if-a-network-port-is-open-in-python#:~:text=To%20check%20if%20a%20network%20port%20is%20open%2C%20call%20socket,connect_ex()%20returns%200%20

# Import Libraries
import socket

# Define variables
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 30 
sockmod.settimeout(timeout)

hostip = input("Enter host IP to scan: ")
portno = input ("Enter specific port to scan: ")
portno = int(portno)

# Define functions
def portScanner(hostip, portno):
    result = sockmod.connect_ex((hostip, portno))
    if result ==0:
        print("Port is OPEN")
    else:
        print("Port CLOSED")

# Main
portScanner(hostip,portno)

# End