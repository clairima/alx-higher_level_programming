#!/usr/bin/python3
"""
This module takes a letter as input, sends a POST request.
with the letter as a parameter, and handles the response accordingly.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request with the given
    letter as a parameter and handles the response.
    Args:
        letter (str): The letter to be sent as a parameter.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
