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
        
# Resources:
    # https://pypi.org/project/cryptography/
    # https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# Import library for encryption
from cryptography.fernet import Fernet

# Declare write key function
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

# Declare load key function to load key from the current directory that is named key.key
def load_key():
    try:
        return open("key.key", "rb").read()
    except:
        return None

# Declare the if key function to write key only if it's not already there
def if_key():
    key = load_key()
    print("Key is: " + str(key.decode('utf-8')))
    if key == None:
        key = write_key()
    return Fernet(key)

#  Declare the encrypt message function for mode 3 and 4
def encrypt_message():
    user_message = input("Enter message would you like to encrypt: ")
    message_encode = user_message.encode()
    f = if_key()
    print("Plaintext message is: " + user_message)
    # encrypt the message
    encrypted = f.encrypt(message_encode)
    print("Encrypted message is: " + str(encrypted.decode('utf-8')))

# Declare decrypt message function for mode 3 and 4
def decrypt_message():
    # Gets user message input to decrypt
    user_input = input("Enter message would you like to decrypt: ")
    message_decode = str.encode(user_input)
    f = if_key()
    # decrypt the message
    decrypted = f.decrypt(message_decode)
    # remove the 'b' and extra ""
    print("Decrypted message is: " + str(decrypted.decode('utf-8')))

# Declare encrypt file function for mode 1 and 2
def encrypt_file():
    f = if_key()
    filename = input("Enter the full filepath for the file you wish to encrypt: ")
    with open(filename, "rb") as file:
        #read file data
        file_data = file.read()
    # encrypt data
    encrypted_file = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_file)

# Declare decrypt file function for mode 1 and 2
def decrypt_file():
    f = if_key()
    filename = input("Enter the full filepath for the file you wish to decrypt: ")
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_doc = file.read()
    #decrypt data
    decrypted_data = f.decrypt(encrypted_doc)
    # write the original file
    with open (filename, "wb") as file:
        file.write(decrypted_data)

def ask_user():
    mode = input("Please pick an actionable option below:\
    \n1. Encrypt a file\
    \n2. Decrypt a file\
    \n3. Encrypt a message\
    \n4. Decrypt a message\
    \n\
    \nPlease enter a number: ")
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
ask_user()

# End