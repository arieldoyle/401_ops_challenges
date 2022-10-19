#!/usr/bin/python3

# Script: Ops 401 Class 12 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 18OCT2022      
# Purpose: 
    # User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
        # Define host IP
    # Define port range or specific set of ports to scan
    # Test each port in the specified range using a for loop
        # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
        # If flag 0x14 received, notify user the port is closed.
        # If no flag is received, notify the user the port is filtered and silently dropped.
    # ICMP Ping Sweep tool
        # Prompt user for network address including CIDR block, for example “10.10.0.0/24” - Careful not to populate the host bits!
        # Create a list of all addresses in the given network
        # Ping all addresses on the given network except for network address and broadcast address
            # If no response, inform the user that the host is down or unresponsive.
            # If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
            # Otherwise, inform the user that the host is responding.
        # Count how many hosts are online and inform the user.
    # In Python, combine the two modes (port and ping) of your network scanner script:
        # Eliminate the choice of mode selection.
        # Continue to prompt the user for an IP address to target.
        # Move port scan to its own function.
        # Call the port scan function if the host is responsive to ICMP echo requests.
        # Print the output to the screen.

# Resources:
    # https://scapy.readthedocs.io/en/latest/installation.html#installing-scapy-v2-x
    # https://scapy.readthedocs.io/en/latest/index.html
    # https://stackoverflow.com/questions/20429674/get-tcp-flags-with-scapy
    # https://resources.infosecinstitute.com/port-scanning-using-scapy/
    # https://stackoverflow.com/questions/63321812/filter-http-get-requests-packets-using-scapy
    # http://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/
# Key Note: 
    # Must install scapy complete bundle and then import library
        # Command: sudo pip install --pre scapy[complete]
    # Script has to be run as sudo (example sudo python3 tcpscanner2.py)

# Import necessary libraries for called functions
from scapy.all import ICMP, IP, sr1, sr, TCP
import random
from ipaddress import IPv4Network

# Declare variables
# Define variable host for host IP
host = input("Enter an IP address to scan: ")

# Define variable port_range providing a port range
port_range = [22, 23, 80, 443, 3389]

# Define functions
# Define ping_port function to do the ICMP and TCP scans
def ping_port(host,port_range):
    # Creates response (rspns variable) to hold port statuses
    rspns = sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)
    if rspns is None:
        print(f"{host} is down or unresponsive.")
    elif (
        int(rspns.getlayer(ICMP).type) == 3 and
        int (rspns.getlayer(ICMP).code) in [1,2,3,9,10,13]):
        print (f"{host} is currently blocking ICMP traffic")
    else:
        print(f"{host} is responding.")
        tcpscan(host,port_range)
           
# Define tcpscan function to search the ports on the host (1)
def tcpscan(host,port_range):     
    for dst_port in port_range:
        # Randomizes the source port (src_port variable)
        src_port = random.randint(1025,65534)
        # Turns the destination port (dst_port variable) into a string
        port_string = str(dst_port)
        # Creates response (rspns variable) to hold port statuses
        rspns = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        # Port Filtered and silently dropped
        if rspns is None:
            print ("Port " + port_string + ": Packet was filtered and dropped")
            print (rspns)
        # Port open for 0x12
        elif rspns.haslayer(TCP):
            if rspns.getlayer(TCP).flags == 0x12: 
                print("Port " + port_string + ": Open")
                # Send RST packet to graciously close open connection
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
                print(rspns)
            # Port closed for 0x14
            if rspns.getlayer(TCP).flags == 0x14:
                print("Port " + port_string + ": Closed")
                print(rspns)

# Main
# calls main function ping_port
ping_port(host,port_range)
    
# End
