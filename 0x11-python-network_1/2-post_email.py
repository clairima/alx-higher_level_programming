#!/usr/bin/python3
"""
This module takes a URL and an email as input, sends a POST request to the URL
with the email as a parameter, and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter and displays the response body.
    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to be sent as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        print("Your email is:", email)
        post_email(url, email)
