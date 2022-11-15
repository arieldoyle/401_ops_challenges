#!/usr/bin/python3
 
# Script: Ops 401 Class 31 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 14NOV2022      
# Purpose: 
    # Prompt the user to type in a file name to search for.
    # Prompt the user for a directory to search in.
    # Search each file in the directory by name.
        # TIP: You may need to perform different commands depending on what OS you’re executing the script on.
    # For each positive detection, print to the screen the file name and location.
    # At the end of the search process, print to the screen how many files were searched and how many hits were found.
    # The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
       
# Resources:
    # https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
    # https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
    # https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python/8220141
    
# Import libraries
from sys import platform
import os, time

# Declare functions

# Function for searching an Linux OS
def linuxSearch():
	# Ask user for a path
    dir = input("Please input the directory you would like to search: ")
	# Ask user for a filename
    file = input("Please input the file you are looking for: ")
	# Count number of files searched and print that number
    os.system("ls " + str(dir) + " | echo \"Searched $(wc -l) files.\"")
	# Count number of files found and print that number
    os.system("find " + str(dir) + ' -name ' + str(file) + " -print | echo \"Found $(grep -c /) matching file(s):\"")
    print("")
    # Print each filename and location found
    os.system("find " + str(dir) + ' -name ' + str(file))
    print("")

# Function for searching a Windows OS
def windowsSearch():
	# Ask user for a path
    dir = input("Please input the directory you would like to search: ")
	# Ask user for a filename
    file = input("Please input the file you are looking for: ")
	# Count number of files searched, store that number in a variable
    searched = os.popen("dir /a:-d /s /b " + str(dir) + " | find /c \":\\\"").read()
    print("Files searched: " + searched)
	# Count number of files found, store that number in a variable
    found = os.popen("dir /b/s " + str(dir) + "\\" + str(file) + " | find /c \":\\\"").read()
    print("Files found: " + found)
	# Print each filename and location found
    os.system("dir /b/s " + str(dir) + "\\" + str(file))

# Main 

# If loop to determine OS and run appropriate function
# Runs def linuxSearch if platform linux(2) is found
if platform == "linux" or platform == "linux2":
    print("This is a Linux machine.")
    linuxSearch()
# Runs def windowsSearch if platform win32 is found    
elif platform == "win32":
    print("This is a Windows machine.")
    windowsSearch()

# End
