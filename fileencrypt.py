#!/usr/bin/python3
 
# Script: Ops 401 Class 06 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 10OCT2022      
# Purpose: 
    # Prompt the user to select a mode:
        # Encrypt a file (mode 1)
            # Prompt the user to provide a filepath to a target file
                # Delete the existing target file and replace it entirely with the encrypted version
        # Decrypt a file (mode 2)
            # Prompt the user to provide a filepath to a target file
                # Delete the encrypted target file and replace it entirely with the encrypted version
        # Encrypt a message (mode 3)
            # Prompt the user to provide a cleartext string
                # Print the ciphertext to the screen
        # Decrypt a message (mode 4)
            # Prompt the user to provide a cleartext string
                # Print the cleartext to the screen
                # Recursively encrypt a single folder and all its contents
        
# Resources:
    # https://pypi.org/project/cryptography/
    # https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# Import library for encryption
from cryptography.fernet import Fernet

# Declare write key function
def write_key():
    # Generates key with Fernet library
    key = Fernet.generate_key()
    # Opens key.key in binary format to write to variable key
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

# Declare load key function to load key from the current directory that is named key.key
def load_key():
    # Looks for key.key to open in binary and read
    try:
        return open("key.key", "rb").read()
    # If none exsist, returns none to key.key value
    except:
        return None

# Declare the if key function to write key only if it's not already there
def if_key():
    # Key variable used load key function to check for key and return a value
    key = load_key()
    # If key value returned None, key will be written by the write key function
    if key == None:
        key = write_key()
    return Fernet(key)

# Declare encrypt file function for mode 1 and 2
def encrypt_file():
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Gets user file path input to encrypt
    filename = input("Enter the full filepath for the file you wish to encrypt: ")
    # Opens the user input file in binary format for reading
    with open(filename, "rb") as file:
        file_data = file.read()
    # Encrypt data
    encrypted_file = f.encrypt(file_data)
    # Opens encrypted file in binary format for writing
    with open(filename, "wb") as file:
        file.write(encrypted_file)

# Declare decrypt file function for mode 1 and 2
def decrypt_file():
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Gets user file path input to decrypt
    filename = input("Enter the full filepath for the file you wish to decrypt: ")
    # Opens the user input file in binary format for reading
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    # Decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # Opens encrypted file in binary format for writing
    with open (filename, "wb") as file:
        file.write(decrypted_data)

#  Declare the encrypt message function for mode 3 and 4
def encrypt_message():
    # Gets user message input to encrypt
    user_message = input("Enter message would you like to encrypt: ")
    # Encodes the message string
    message_encode = user_message.encode()
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Prints out message user put in in plaintext
    print("Plaintext message is: " + user_message)
    # Encrypt the message
    encrypted = f.encrypt(message_encode)
    # Prints encrypted message
    print("Encrypted message is: " + str(encrypted.decode('utf-8')))

# Declare decrypt message function for mode 3 and 4
def decrypt_message():
    # Gets user message input to decrypt
    user_message = input("Enter message would you like to decrypt: ")
    # Decodes the message string
    message_decode = str.encode(user_message)
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Decrypt the message
    decrypted = f.decrypt(message_decode)
    # Prints decrypted message into plaintext
    print("Decrypted plaintext message is: " + str(decrypted.decode('utf-8')))

def user_prompt():
    # Asks user for mode input
    mode = input("Please pick an actionable option below:\
    \n1. Encrypt a file\
    \n2. Decrypt a file\
    \n3. Encrypt a message\
    \n4. Decrypt a message\
    \n\
    \nPlease enter a number: ")
    # If statements for above functions/actions
    if (mode == "1"):
        encrypt_file()
        print("...file encrypted.")
    elif (mode == "2"):
        decrypt_file()
        print("...file decrypted.")
    elif (mode == "3"):
        encrypt_message()
    elif (mode == "4"):
        decrypt_message()
    else:
        print("Invalid input")

# Main
# Runs the ask user function
user_prompt()

# End
