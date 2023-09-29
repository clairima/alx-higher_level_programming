#!/usr/bin/python3
"""
This module takes a URL and an email address as input,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter and displays the response body.
    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to be sent as a parameter.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print("Your email is:", email)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
