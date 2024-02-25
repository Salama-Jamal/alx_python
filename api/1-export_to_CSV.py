import requests
import sys
import csv
from sys import argv

def export_to_CSV(employee_id):
    """ Export employee's TODO list data to a CSV file """

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # GET requests to fetch user details and TODO list
    users_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Extract JSON data from responses
    user_data = users_response.json()
    todos_data = todos_response.json()

    # Extract user information
    user_id = user_data['id']
    username = user_data['username']

    # Prepare list to store task data
    tasks_rows = []

    # Iterate over todo items and extract relevant information
    for todo in todos_data:
        task_completed_status = str(todo['completed'])
        task_title = todo['title']
        tasks_rows.append([user_id, username, task_completed_status, task_title])

    # Write task data to a CSV file
    filename = f"{user_id}.csv"
    with open(filename, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Write header
        csvWriter.writerows(tasks_rows)

    print(f"CSV file '{filename}' created successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_CSV(employee_id)
