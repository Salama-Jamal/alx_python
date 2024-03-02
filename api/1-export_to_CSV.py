import csv
import requests
import sys


employee_id = int(sys.argv[1]) 

#fetching employee general details
employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = employee_details.json()

#fetching employee todo list details
employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos_details = employee_todos.json()

def todo_list_progress(employee_id):
    
    #fetching employee name
    employee_name = employee_data["name"]
    
    #fetching employee total todo list length and completed tasks
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])
    
    #printing employee todo list progress          
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for todo in todos_details:
        if todo["completed"]:
            print(f"\t {todo['title']}")
            
    
def write_to_csv(employee_id, employee_name, todos_details):
     with open("USER_ID.csv", "w", newline="") as csvfile:
         fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         
         writer.writeheader()
         for todo in todos_details:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS":str(todo['completed']),
                "TASK_TITLE": todo['title']
            })
        
if __name__ == "__main__":   
    todo_list_progress(employee_id)
    write_to_csv(employee_id, employee_data['name'], todos_details)
