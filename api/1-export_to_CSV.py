import csv
from task0 import get_employee_tasks

def export_to_CSV(user_id):
    tasks = get_employee_tasks(user_id)
    file_name = f"{user_id}.csv"
    
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for task in tasks:
            writer.writerow({"USER_ID": user_id, "USERNAME": task["username"], "TASK_COMPLETED_STATUS": task["completed"], "TASK_TITLE": task["title"]})

if __name__ == "__main__":
    import sys
    user_id = int(sys.argv[1])
    export_to_CSV(user_id)
