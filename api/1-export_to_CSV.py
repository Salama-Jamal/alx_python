import csv
import sys

# Sample data
tasks_data = {
    2: [
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "suscipit repellat esse quibusdam voluptatem incidunt"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "distinctio vitae autem nihil ut molestias quo"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "et itaque necessitatibus maxime molestiae qui quas velit"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "adipisci non ad dicta qui amet quaerat doloribus ea"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "voluptas quo tenetur perspiciatis explicabo natus"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "aliquam aut quasi"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "veritatis pariatur delectus"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "nesciunt totam sit blanditiis sit"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "laborum aut in quam"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "repudiandae totam in est sint facere fuga"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "earum doloribus ea doloremque quis"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "sint sit aut vero"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "porro aut necessitatibus eaque distinctio"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "repellendus veritatis molestias dicta incidunt"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "excepturi deleniti adipisci voluptatem et neque optio illum ad"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "sunt cum tempora"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "totam quia non"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "False", "TASK_TITLE": "doloremque quibusdam asperiores libero corrupti illum qui omnis"},
        {"USER_ID": "2", "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": "True", "TASK_TITLE": "totam atque quo nesciunt"}
    ]
}

def export_to_csv(user_id):
    if user_id in tasks_data:
        filename = f"{user_id}.csv"
        with open(filename, mode='w', newline='') as file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks_data[user_id]:
                writer.writerow(task)
        print(f"Data exported to {filename} successfully.")
    else:
        print("User ID not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py USER_ID")
    else:
        user_id = int(sys.argv[1])
        export_to_csv(user_id)
