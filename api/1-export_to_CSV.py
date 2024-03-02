import csv
import requests
import sys 

def fetch_todo_list_progress(employee_id):
    # Fetching employee details
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']


    # Fetching todo list for the employee
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()


    # Counting completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    #num_completed_tasks = len(completed_tasks)
    #total_tasks = len(todo_data)


    # Writting data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

    # Return the number of tasks in the CSV file
    return len(todo_data)


    # Printing employee todo list progress
    #print(
    #    f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    #for task in completed_tasks:
    #    print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    num_tasks = fetch_todo_list_progress(employee_id)
    print(f"Number of tasks in CSV: {num_tasks}")
