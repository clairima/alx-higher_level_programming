#!/usr/bin/python3
"""
This module takes a URL as input, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

def fetch_x_request_id(url):
    """
    Fetches the given URL and prints the value of X-Request-Id from the response header.
    Args:
        url (str): The URL to send the request to.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <URL>")
    else:
        url = sys.argv[1]
        fetch_x_request_id(url)
