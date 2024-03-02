"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user information """

    # Calculate total number of tasks from API
    total_tasks = sum(1 for task in requests.get(todos_url).json() if task['userId'] == id)

    # Count number of tasks in CSV file
    num_tasks_in_csv = 0
    with open(str(id) + ".csv", 'r') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)
        for _ in reader:
            num_tasks_in_csv += 1

    # Compare total tasks with tasks in CSV
    if total_tasks == num_tasks_in_csv:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    user_info(int(sys.argv[1]))
