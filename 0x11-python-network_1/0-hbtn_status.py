#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using urllib.
It prints the response body information including type,
content, and UTF-8 content.
"""

import urllib.request


def fetch_url():
    """
    Fetches URL and prints response body information.
    """
    with urllib.request.urlopen(
        "https://alx-intranet.hbtn.io/status"
    ) as response:
        body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_url()
