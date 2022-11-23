#!/usr/bin/env python3

# Script: Ops 401 Class 16 Ops Challenge Solution
# Author: Ariel D.                  
# Date of latest revision: 22NOV2022     
# Purpose: 
    # The below Python script shows one possible method to return the cookie from a site that supports cookies.
    # Add here code to make this script perform the following:
        # Send the cookie back to the site and receive a HTTP response
        # Generate a .html file to capture the contents of the HTTP response
        # Open it with Firefox
    # Stretch Goal
        # Give Cookie Monster hands
# Resources:
    # https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/
    # https://github.com/codefellows/seattle-ops-401d5/blob/main/class-37/challenges/DEMO.md
    # https://stackoverflow.com/questions/50329050/save-load-html-response-as-object-in-a-file-python
# Key Note: 
    # 
    
# Import required libraries
import requests, os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is: " + targetsite)
print(cookie)

html = requests.get(targetsite, cookies=cookie)
content = html.text

with open ('cookiefile.html', 'w') as f:
  f.write(content)

print("Opening website....")

os.system("firefox /home/kali/Desktop/cookiefile.html")
