#!/usr/bin/python3
"""
This module takes a URL as input, sends a request to the URL,
displays the body of the response (decoded in utf-8), and handles HTTP errors.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Fetches the given URL, handles HTTP errors, and prints the response body.
    Args:
        url (str): The URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <URL>")
    else:
        url = sys.argv[1]
        fetch_url(url)
