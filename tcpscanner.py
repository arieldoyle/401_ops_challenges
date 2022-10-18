#!/usr/bin/python3

# Script: Ops 401 Class 11 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 17OCT2022      
# Purpose: 
    # Define host IP
    # Define port range or specific set of ports to scan
    # Test each port in the specified range using a for loop
        # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
        # If flag 0x14 received, notify user the port is closed.
        # If no flag is received, notify the user the port is filtered and silently dropped.
# Resources:
    # https://scapy.readthedocs.io/en/latest/installation.html#installing-scapy-v2-x
    # https://scapy.readthedocs.io/en/latest/index.html
    # https://stackoverflow.com/questions/20429674/get-tcp-flags-with-scapy
    # https://resources.infosecinstitute.com/port-scanning-using-scapy/
# Key Note: 
    # Must install scapy complete bundle and then import library
        # Command: sudo pip install --pre scapy[complete]
    # Script has to be run as sudo


# Import necessary libraries for called functions
from scapy.all import ICMP, IP, sr1, sr, TCP
import random

# Declare variables
# Define variable host for host IP
host = "scanme.nmap.org" 

# Define variable port_range providing a port range
port_range = [21, 22, 23] 

# Main
# Send SYN with random source ports for each destination port
for dst_port in port_range:
    src_port = random.randint(1025,65534)
    port_string = str(dst_port)
    rspns = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
    if rspns is None:
        # Port Filtered and silently dropped
        print ("Port " + port_string + ": Packet was filtered and dropped")
        print (rspns)
    elif rspns.haslayer(TCP):
        # Port open for 0x12
        if rspns.getlayer(TCP).flags == 0x12: 
            print("Port " + port_string + ": Open")
            # Send RST packet to graciously close open connection
            send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
            print(rspns)
        # Port closed for 0x14
        if rspns.getlayer(TCP).flags == 0x14:
            print("Port " + port_string + ": Closed")
            print(rspns)
     
# End
