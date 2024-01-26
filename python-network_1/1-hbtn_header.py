#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and
displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Display the value of X-Request-Id in the response header
        print(response.headers.get('X-Request-Id'))
    else:
        print("Error: Request failed with status code {}".format(response.status_code))