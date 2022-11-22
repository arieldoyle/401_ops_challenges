#!/usr/bin/python3

# Script: Ops 401 Class 16 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 24OCT2022      
# Purpose: 
    # Prompts the user to type a URL or IP address.
    # Prompts the user to type a port number.
    # Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
    # Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
    # Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
# Resources:
    # https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
    # https://www.instructables.com/Netcat-in-Python/
# Key Note: 
    # Be sure to only target approved URLs like scanme.nmap.org or web servers you own
    

# Import required libraries
import socket, subprocess, os

# Declare Functions
# Declare netcat fingerprinting function
def netcat(a, p):
    print("Netcat: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))

    run = "nc " + a + " " + p
    sock.sendall(run.encode())
    sock.shutdown(socket.SHUT_WR)

    res = " "

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()

# Declare telnet fingerprinting function
def telnet(a, p):
    print("Telnet: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))

    run = "telnet " + a + " " + p
    sock.sendall(run.encode())
    sock.shutdown(socket.SHUT_WR)

    res = " "

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()

# Declare nmap fingerprinting function
def nmap(addr, port):
    print("Nmap...")
    os.system("nmap -Pn -p " + port + " -sV -script=banner " + addr + " | grep banner")

# Main
print("Welcome to the Web Application Fingerprinting Tool....")

a = input("Type in a URL or IP address you'd like to fingerprint: ")
p = input("What port would you like to check: ")

netcat(a, p)
telnet(a, p)
nmap()

# End