#!/usr/bin/python3
 
# Script: Ops 401 Class 33 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 16NOV2022      
# Purpose: 
    # Prompt the user to type in a file name to search for.
    # Prompt the user for a directory to search in.
    # Search each file in the directory by name.
        # TIP: You may need to perform different commands depending on what OS you’re executing the script on.
    # For each positive detection, print to the screen the file name and location.
    # At the end of the search process, print to the screen how many files were searched and how many hits were found.
    # The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
    # Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
    # For each file scanned within the scope of your search directory:
        # Generate the file’s MD5 hash using Hashlib.
        # Assign the MD5 hash to a variable.
        # Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
    # Staging:
        # Copy and paste the demo script into a new Python file on your system.
        # Download virustotal-search.py and place it in the same folder as the demo Python script.
        # Sign up for an account at virustotal.com to get a free API key.
        # To query the VirusTotal API, you’ll need to set your API key as an environment variable to avoid hard-coding it into your demo Python script, which is currently set to call “API_KEY_VIRUSTOTAL” in place of your literal API key. You can always hard-code it at first for testing, but don’t leave it that way!
        # Set the variable hash to whatever MD5 hash you wish to VirusTotal to evaluate.
    # Successfully connect to the VirusTotal API
    # Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
    # Print to the screen the number of positives detected and total files scanned

# Resources:
    # https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
    # https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
    # https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python/8220141
    # https://docs.python.org/3/library/hashlib.html
    # https://www.programiz.com/python-programming/examples/hash-file
    # https://developers.virustotal.com/reference#file-scan
    # https://www.tines.io/blog/virustotal-api-security-automation
    # https://www.youtube.com/watch?v=D925hYZjKY0&t=359s&ab_channel=EduardMarian
    # https://github.com/eduardxyz/virustotal-search

# Import libraries
from sys import platform
import os, time, datetime, math
from matplotlib.pyplot import pause
import hashlib

# Declare functions

# Function for searching an Linux OS
def platformCheck():
    # Intro to the OS checker
    print("Please standby by while we determine what operating system you are running.......")
    pause(2)
    # If loop to determine OS and run appropriate function
    # Runs def linuxSearch if platform linux(2) is found
    if platform == "linux" or platform == "linux2":
        print("This is a Linux machine. \nPlease standby. Starting up the Signature Malware Detection Tool......")
        linuxSearch()
        pause(2)

    # Runs def windowsSearch if platform win32 is found    
    elif platform == "win32":
        print("This is a Windows machine. \nPlease standby. Starting up the Signature Malware Detection Tool......")
        pause(2)
        windowsSearch()

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

# Function to get current time and date and store it
def timeStamp():
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')

# Function that uses the virus-search.py to compare target file's md5 hash with the entries on VirusTotal API to check for known malware signatures
def checkForMalware():
    # You'll need a free API key from virustotal.com (need to sign up first)
    apiKey = os.getenv('API_KEY_VIRUSTOTAL') 
    # hash = ''     # Used to hardcode hash for testing
    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + apiKey + ' -m ' + hash

    os.system(query)

# Function that opens, reads it by a set block by block and returns the hex 
def hash_file(filename):
   # Make a hash object
   hashTag = hashlib.md5()
   # Open file for reading in binary mode
   with open(filename,'rb') as file:
       # Loop till the end of the file
       block = 0
       while block != b'':
           # read only 1024 bytes at a time
           block = file.read(1024)
           hashTag.update(block)
   # Return the hex representation of digest
   return hashTag.hexdigest()

# Function that os.walks through directories and displays hash of all files found within that directory
def getHash():
    dir_c = 0
    file_c = 0
    start_p = input("Please enter the absolute path to the directory you want to get the file hashes for: ")
    for (path,dirs,files) in os.walk(start_p):
        print('DIRECTORY: {:s}'.format(path))
        print("")
        dir_c += 1
        #Repeats for each file in selected directory     
        for file in files:
            fstat = os.stat(os.path.join(path,file))
            # Convert file size to MegaBytes, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                filesize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                filesize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                filesize = fstat.st_size
                unit = "B"
            file_c += 1
            filename = os.path.join(path,file)
            md5 = hash_file(filename)
            timestamp = timeStamp()
            print(timestamp)
            print(f"FILENAME: {file}\tSIZE: {str(filesize) + unit} \tPATH: {filename} \tHASH: " + md5 + "\n")
    # Print summary on total fileshashed and directory count
    print('Summary: hashed {} files in {} directories'.format(file_c,dir_c))
    dir_c = 0
    file_c = 0  

# Function for asking for user prompt on main menu
def userPrompt():
    # Tool introduction and asks user for mode input
    print("Welcome to the Signature-based Malware Detection Tool Command Home.")
    mode = input("Please pick an actionable option below:\
    \n1. Check OS, Search for a file\
    \n2. Get File Hashes for all files in a directory\
    \n\
    \nPlease enter a number: ")
    # If statements for above functions/actions
    if (mode == "1"):
        platformCheck()
    elif (mode == "2"):
        getHash()
    else:
        print("Invalid input")

# Main 
userPrompt()

# End
