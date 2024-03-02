#!/usr/bin/python3 

"""
this is a python file that export it's data to csv"""
import csv
import requests 
import sys 

def get_employee_tasks(user_id):
    """Get the endpoint"""
    employee_url = "https://jsonplaceholder.typicode.com/users/{}"
    employee_response = requests.get(employee_url.format(user_id))
     
    #  if status code is correct get employee details
    if employee_response.status_code == 200:
        employee_details = employee_response.json()
        user_id = employee_details['id']
        username = employee_details['username']
    else: 
        print(f"Failed to retrieve employee's details:{employee_response.status_code}")
        return None
    
    
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_response = requests.get(todo_url)
    

    if todo_response.status_code == 200:
        task_data = todo_response.json()
    else:
        print(f"Failed to retrieve employee's todos:{employee_response.status_code}")
        return None

    csv_filename = f"{user_id}.csv"
    with open(str(user_id) + ".csv", 'w', newline="") as f:


         fieldnames = ['user_id', 'username', 'task_completed_status', 'task_title']
         writer = csv.DictWriter(f, fieldnames=fieldnames)
        
         row = [{
                 'user_id': user_id,
                 'username': username,
                 'task_completed_status': task['completed'],
                 'task_title': task['title']
                 } for task in task_data]
         writer.writerows(row)
                 
             
    print(f"The csv_file{csv_filename} was successfully created with data from {user_id}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
         user_id = int(sys.argv[1])
    else:
      user_id = 1
      get_employee_tasks(user_id)
         
