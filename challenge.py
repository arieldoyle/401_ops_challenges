#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: OPS 401d5 Class 38 Ops Challenge
# Date:        TODO: 23NOV2022
# Modified by: TODO: Ariel R Doyle

# Objectives:
    # Fully annotate any missing comments and populate any missing variables/code
    # Test the script in Web Security Dojo to confirm the output is correct
    # This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame
    # This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php

# Resources:
    # https://www.thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python
    # https://www.thepythoncode.com/article/sql-injection-vulnerability-detector-in-python

# Key Notes: 
    # Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# This function submits the forms from the dictionary containing form details created by the get_form_details function and populates the input fields with strings contained in the value. Constructs full url only if a relative path is given. Form is submitted via GET or POST request
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# The function below creates soup 'objects' out of the forms and puts them in the details = {} list and continues on to gather details of each action and method form and input attribute
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# This function submits the forms from the dictionary containing form details created by the get_form_details function and populates the input fields with the strings contained in value. Constructs full url only if a relative path is given. Frm is submitted via GET or POST request
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Once given a url, this function grabs all the HTML forms and prints out the number of forms detected. It moves through each form, submitting with js_script insertion. If Javascript is successfully passed and executed, the variable is_vulnerable is deemed True. The function will then return the vale of is_vulnerable to indicate whether or not the web page in question is actually susceptible and vulnerable to XSS attacks
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('You have vulnerabilities and are being tracked.')</script>
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

# "__name__" evaluates to the name of the current module; Directing the script to execute the commands beneath it when running in the terminal - in this case, it asks the user to input a URL to test, and then runs that URL through the scan_xss function and prints out the results
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearly indicating which is positive detection and negative detection

# DVWA Reflected Cross Site Scripting page
# Negative Detection
# dojo@dojo-VirtualBox:~/Desktop$ python3 challenge.py
# Enter a URL to test for XSS:http://dvwa.local/vulnerabilities/xss_r/
# [+] Detected 1 forms on http://dvwa.local/vulnerabilities/xss_r/.

# DVWA Reflected Cross Site Scripting page
# Positive Detection
# dojo@dojo-VirtualBox:~/Desktop$ python3 challenge.py
# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': "<script>alert('You have vulnerabilities and are being tracked.')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
