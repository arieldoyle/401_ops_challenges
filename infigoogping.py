#!/usr/bin/python3

# Script: Ops 401 Class 02 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 04OCT2022      
# Purpose: 
    # Transmit a single ICMP (ping) packet to a specific IP every 2 seconds
    # Evaluate the response as either success or fail
    # Assign success or failure to a status variable
    # For every ICMP transmission attempted, pring the status variable along with a comprehensive timestamp and destinatino IP tested
# Resources:
    # https://stackoverflow.com/questions/26468640/python-function-to-test-ping

# Import necessary libraries for called functions
import datetime, time, os

# Declare hello_ping function
def hello_ping():

    # Declare variable host for Google.com
    host = "8.8.8.8"

    # Declare variable status
    status = os.system("ping -c 1 " + host)

    # Checks status variable for successful or failed ping based on output
    if status == 0:
        answer = " Network ACTIVE to 8.8.8.8 "
    else:
        answer = " Network ERROR to 8.8.8.8 "
    return answer
    
# Declare answer equal to hello_ping function
answer = hello_ping()

# Declare variable now for current date and time
now = datetime.datetime.now()

# Print string
print("Current date and time: ")

# Print now variable as string
print(str(now))

# Declare ping_test function to get timestamps of ping every 2 seconds
# Infinite while loop to ping and print out ping status/data

def ping_test():
    while True:
        # Print start time ping
        print("Start : %s" % time.ctime())

        print(answer)

        # Pause action for 2 seconds
        time.sleep(2)

        # Print end time of ping
        print("End : %s" % time.ctime())

# Main
# Calls ping_test function
ping_test()

# End