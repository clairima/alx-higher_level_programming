#!/usr/bin/python3
"""
This module takes a URL as input, sends a request to the URL,
displays the response body,
and prints the HTTP status code if it's greater than or equal to 400.
"""

import requests
import sys


def fetch_url(url):
    """
    Fetches the given URL, displays the response body, and handles HTTP errors.
    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    print(response.text)
    if response.status_code >= 400:
        print("Error code:", response.status_code)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
