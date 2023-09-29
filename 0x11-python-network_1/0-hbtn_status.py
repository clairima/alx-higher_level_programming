#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using urllib.
It prints the response body information including type, content, and UTF-8 content.
"""

import urllib.request

def fetch_url(url):
    """
    Fetches the given URL and prints response body information.
    Args:
        url (str): The URL to fetch.
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", utf8_content)

if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")
