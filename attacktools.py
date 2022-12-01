#!/usr/bin/python3

# Script: Ops 401 Class 42 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 01DEC2022      
# Purpose: 
    # Finish DEMO.md in your class repo > Class 42 > Challenges folder.
# Resources:
    # https://pypi.org/project/python-nmap/
# Key Note: 
    # Install Nmap library for Python by running sudo pip3 install python-nmap

# Import Libraries

import nmap

# Define variables

scanner = nmap.PortScanner()

# Define functions

def syn_ack():
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def udp():
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print("protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

def os():
    print("Nmap Version: ",scanner.nmap_version())
    print(scanner.scan(ip_addr, arguments='-O')['scan'][ip_addr]['osmatch'][0])

### Menu of options ###
def menu():
    resp = input("""\nSelect scan to execute:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Operating System\n""")
    print("You have selected option: ", resp)

    if (resp == "1"):
        syn_ack()
    elif (resp == "2"):
        udp()
    elif (resp== "3"):
        os()
    else:
        print("Invalid input")

# Main

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

range = input("Enter port range (e.g. 1-50): ")

menu()