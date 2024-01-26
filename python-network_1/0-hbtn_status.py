#!/usr/bin/python3
"""
Script that fetches https://alu-intranet.hbtn.io/status
using the requests package.
"""

import requests

def fetch_status(url):
    """
    Fetches the status from the given URL using the requests package.

    Args:
        url (str): The URL to fetch.

    Returns:
        requests.models.Response: The response object.
    """
    response = requests.get(url)
    return response

def display_response_info(response):
    """
    Displays information about the response.

    Args:
        response (requests.models.Response): The response object.
    """
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = fetch_status(url)
    display_response_info(response)