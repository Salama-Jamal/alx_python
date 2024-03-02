import csv
import requests
import sys

def employee_info(employee_id):
    """Retrieve employee details and tasks from the given URL."""
    # Construct URLs for employee details and tasks
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Make HTTP GET requests to fetch data
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    # Extract relevant information from the responses
    employee_data = employee_response.json()
    todos_data = todos_response.json()

    # Initialize a list to store task details
    tasks = []

    # Extract task details
    for task in todos_data:
        task_details = (
            employee_id,
            employee_data['username'],
            task['completed'],
            task['title']
        )
        tasks.append(task_details)

    """creating csv file for the empoyee"""
    file_name = f"{employee_id}.csv"
    with open(file_name, "w", newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE' ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        """Write the csv headers"""
        writer.writeheader()

        """Write the rows under the epecified columns"""
        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_data['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id.")
        sys.exit(1)

    # Extract employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to retrieve and record employee task details
    employee_info(employee_id)
