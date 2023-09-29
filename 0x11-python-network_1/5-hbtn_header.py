#!/usr/bin/python3
"""
This module takes a URL as input, sends a request to the URL,
and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

def fetch_x_request_id(url):
    """
    Sends a request to the given URL and displays the value of X-Request-Id from the response header.
    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
