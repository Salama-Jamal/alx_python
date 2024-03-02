# python program to export file in json as dictionary

import requests
import sys

def get_employee_info(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if not employee_data:
        print(f"Error: Employee with ID {employee_id} not found.")
        return
    employee_name = employee_data['name']

    # fetching the TODO list for the employee
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # calculating the TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # to output employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # to output titles of completed taskes
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
