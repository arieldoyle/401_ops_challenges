#!/usr/bin/python3

# Script: Ops 401 Class 03 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 05OCT2022      
# Purpose: 
    # Ask the user for an email address and password to use for sending notifications.
    # Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
    # Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event. 

# Resources:
    # https://stackoverflow.com/questions/26468640/python-function-to-test-ping
    # https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
    # https://realpython.com/python-send-email/

# Import necessary libraries for called functions
import datetime, os, smtplib, ssl, time

# A way to keep the password from displaying on the screen
from getpass import getpass

# Declare variables
down = " Network is DOWN "
up = "Network is UP "
ping_status = 0
last = 0
now = datetime.datetime.now()
smtp_server = "smtp.gmail.com"
port = 465
sender_email = "my@gmail.com"

# Prompt user for email
user_email = input("Please enter your email to send network updates to: ")

# Prompt user for password
password = getpass("Please enter your email account password: ")

# Prompt user for ip
ipaddress = input("Please input the IP address you would like to monitor and get updates for: ")


# Declare active_alert function to get network status, open SMTP server, send ACTIVE email, and close SMTP server
def active_alert():
    print("Timestamp : %s" % time.ctime())
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.ehlo()
    server.login(user_email, password)
    active_msg = "Salutations! Your system is ACTIVE as of: %s" % time.ctime()
    server.sendmail(sender_email, user_email, active_msg)
    server.quit()

# Declare error_alert function to get network status, open SMTP server, send ERROR email, and close SMTP server
def error_alert():
    print("Timestamp : %s" % time.ctime())
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.ehlo()
    server.login(user_email, password)
    down_msg = "Salutations! Your system is DOWN as of: %s" % time.ctime()
    server.sendmail(sender_email, user_email, down_msg)
    server.quit()    

# Declare ping_alert function to check for network status changes and create a response
def ping_alert():
    print("Timestamp : %s" % time.ctime())

    global ping_status
    global last

    if (( ping_status != last ) and ( ping_status == up )):
        last = up
        active_alert()
    elif (( ping_status != last ) and ( ping_status == down )):
        last = down
        error_alert()

    ping = os.system("ping -c 1 " + ipaddress)

    if ping == 0:
        ping_status = up
    else:
        ping_status = down
        print("Timestamp : %s" % time.ctime() + ping_status + "to: " + ipaddress)

# Main
while True:
    ping_alert()
    time.sleep(2)

# End