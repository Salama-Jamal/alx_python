"""fetching employee,TODO lists and counting completed tasks
"""

import csv
import requests
import sys

def fetch_user_info(user_id):
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}users/{}'.format(url, user_id)
    response = requests.get(user_url)
    user_info = response.json()
    return user_info


def fetch_user_todos(user_id):
    url = 'https://jsonplaceholder.typicode.com/'
    todos_url = '{}todos?userId={}'.format(url, user_id)
    response = requests.get(todos_url)
    todos = response.json()
    return todos


def export_to_csv(user_id, user_info, todos):
    filename = '{}.csv'.format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for todo in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user_info['username'],
                'TASK_COMPLETED_STATUS': 'Completed' if todo['completed'] else 'Incomplete',
                'TASK_TITLE': todo['title']
            })
    print(f"CSV file '{filename}' has been created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_info = fetch_user_info(user_id)
    todos = fetch_user_todos(user_id)
    export_to_csv(user_id, user_info, todos)
