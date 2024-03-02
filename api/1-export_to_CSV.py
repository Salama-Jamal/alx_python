import sys
import csv
import requests

# Function to fetch employee data from the API
def fetch_employee_data(employee_id):
    try:
        # Fetch employee details
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        response.raise_for_status()
        employee_data = response.json()
        
        # Fetch employee's TODO list
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        response.raise_for_status()
        todos_data = response.json()
        
        return employee_data, todos_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

# Function to export data to CSV file
def export_to_csv(employee_id, employee_data, todos_data):
    try:
        filename = f"{employee_id}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos_data:
                writer.writerow([employee_id, employee_data['username'], str(todo['completed']), todo['title']])
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    
    employee_id = int(employee_id)
    employee_data, todos_data = fetch_employee_data(employee_id)
    export_to_csv(employee_id, employee_data, todos_data)
