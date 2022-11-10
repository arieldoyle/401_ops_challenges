#!/usr/bin/python3

# Script: Ops 401 Class 27 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 08NOV2022      
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
        # Recursively encrypt a single folder and all its contents (mode 5)
        # Recursively decrypt a single folder that was encrypted by this tool (mode 6)
        # Add logging capabilities to your Python tool using the logging library.
        # Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory.
        # Confirm your logging feature is working as expected.
        # Add a log rotation feature based on size

# Resources:
    # https://pypi.org/project/cryptography/
    # https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
    # https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/
    # https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
    # https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    # https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/
    # https://dotnettutorials.net/lesson/logging-module-in-python/
    
# Import library for encryption
from fileinput import filename
from cryptography.fernet import Fernet
from posixpath import dirname
import os, os.path
import logging
from logging.handlers import RotatingFileHandler

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
    # Prints to the screen the key value
    # print("Key is: " + str(key.decode('utf-8'))) *will only work if key.key is found*
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

# Declare r encrypt folder function 
def r_encrypt(filename):
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Opens folder and contents in binary format for reading
    with open(filename, "rb") as file:
        folder_data = file.read()
    encrypted_folder = f.encrypt(folder_data)
    # Opens encrypted folder and contents in binary format for writing
    with open(filename, "wb") as file:
        file.write(encrypted_folder)

# Declare r decrypt folder function
def r_decrypt(filename):
    # Variable that checks for the key.key (uses if_key function)
    f = if_key()
    # Opens encrypted folder and contents in binary format for writing
    with open(filename, "rb") as file:
        encrypted_folder = file.read()
    # Decrypts folder
    decrypted_folder = f.decrypt(encrypted_folder)
    # Opens decrypted folder and contents in binary format for writing
    with open(filename, "wb") as file:
        file.write(decrypted_folder)

# Defines folder encrypt function for mode 5
def folder_encrypt():
    # Gets user folder path input for encrypting
    folder_path = input("Enter the path to the folder you want to encrypt: ")
    # Looks for folder and contents
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # Prints folder path to screen
        print('Folder: {:s}'.format(dirpath))
        # Encrypts files within the folder
        for file in filenames:
            filename = os.path.join(dirpath,file)
            r_encrypt(filename)
    # Prints completion of folder and content encryption
    print("Folder and contents have been encrypted.")
        
# Defines folder decrypt function for mode 6
def folder_decrypt():
    # Gets user folder path input for decrypting
    folder_path = input("Enter the path to the folder you want to decrypt (previously encrypted by this tool ONLY): ")
    # Looks for folder and contents
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # Prints folder path to screen
        print('Folder: {:s}'.format(dirpath))
        # Decrypts files witin the folder
        for file in filenames:
            filename = os.path.join(dirpath,file)
            r_decrypt(filename)
    # Prints completion of folder and content decryption
    print("Folder and contents have been decrypted.")

def user_prompt():
    # Asks user for mode input
    mode = input("Please pick an actionable option below:\
    \n1. Encrypt a file\
    \n2. Decrypt a file\
    \n3. Encrypt a message\
    \n4. Decrypt a message\
    \n5. Encrypt a folder and contents\
    \n6. Decrypt a folder and contents (previously encrypted by this tool ONLY)\
    \n\
    \nPlease enter a number: ")
    # If statements for above functions/actions
    if (mode == "1"):
        encrypt_file()
    elif (mode == "2"):
        decrypt_file()
    elif (mode == "3"):
        encrypt_message()
    elif (mode == "4"):
        decrypt_message()
    elif (mode == "5"):
        folder_encrypt()
    elif (mode == "6"):
        folder_decrypt()
    else:
        print("Invalid input")

# Main

logs = logging.getLogger('log')
logs.setLevel(logging.INFO)
handler = RotatingFileHandler('log', maxBytes=500, backupCount=3)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logs.addHandler(handler)
print('Logging in process')

for i in range(200):
    logmsg = "Warning: Script is running but should be checked"
    logmsg += str(i)
    logs.warning(logmsg)
    logs.info('Info: Script is running.')
    logs.critical('Critical: Issue encountered!')
    logs.error('Error: Script has stopped functioning properly.')

try:
    user_prompt()

except Exception as msg:
    print(msg)
    logging.exception(msg)

print('Logging complete.')

# End