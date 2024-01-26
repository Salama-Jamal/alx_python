#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
prints: Error code: followed by the value of the HTTP status code.
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

    # Display the body of the response
    print(response.text)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))