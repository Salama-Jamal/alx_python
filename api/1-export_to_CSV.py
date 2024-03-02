"""Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv """

import csv
import requests
import sys


def get_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    response = requests.get(user_url)
    return response.json()


def get_user_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    todos_url = "{}todos?userId={}".format(url, user_id)
    response = requests.get(todos_url)
    return response.json()


def display_user_progress(user_data, tasks):
    print("Employee {} is done with tasks".format(user_data.get("name")), end="")

    completed_tasks = [task for task in tasks if task.get("completed")]

    print("({}/{}):".format(len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


def export_to_csv(user_id, user_data, tasks):
    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow(
                {
                    "USER_ID": user_data.get("id"),
                    "USERNAME": user_data.get("username"),
                    "TASK_COMPLETED_STATUS": str(task.get("completed")),
                    "TASK_TITLE": task.get("title"),
                }
            )


def record_and_export(user_id):
    user_data = get_user_data(user_id)
    if not user_data:
        print(f"Error: User not found for ID {user_id}")
        sys.exit(1)

    user_tasks = get_user_tasks(user_id)

    display_user_progress(user_data, user_tasks)

    try:
        export_to_csv(user_id, user_data, user_tasks)
        print("Export to CSV: Success")
    except Exception as e:
        print(f"Export to CSV: Error - {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    record_and_export(user_id)
