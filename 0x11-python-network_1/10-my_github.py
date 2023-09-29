#!/usr/bin/python3
"""
This module takes a GitHub username and personal access token as input,
uses Basic Authentication to access the GitHub API, and displays the user id.
"""

import requests
import sys


def get_github_user_id(username, token):
    """
    Sends a GET request to GitHub API using
    Basic Authentication and displays the user id.
    Args:
        username (str): GitHub username.
        token (str): Personal access token (password) for authentication.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <username> <token>")
    else:
        username = sys.argv[1]
        token = sys.argv[2]
        get_github_user_id(username, token)
