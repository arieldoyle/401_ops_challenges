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
# Resources:
    # https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
    # https://www.kaggle.com/wjburns/common-password-list-rockyoutxt (For the word list to search)
# Key Note: 
    # File path to rockyou.txt


# Import necessary libraries for called functions
import time, getpass

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

# Defines function that asks user for a common password and checks if it is held within the file in the file path by opening, reading, and outputs the results of the search
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

# Main

# If statments that run this when bruteforce.py is ran on the computer, and only exit when 3 is input
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive: Dictionary Iterator
2 - Defensive: Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            password_check()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 


# End