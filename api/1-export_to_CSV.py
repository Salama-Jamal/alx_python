import csv
import requests
from sys import argv

def export_to_CSV(sizeofReq):
    
    allTasks = []

    link = "https://jsonplaceholder.typicode.com"

    usersRes = requests.get("{}/users/{}".format(link, sizeofReq))
    todosRes = requests.get("{}/users/{}/todos".format(link, sizeofReq))

    name = usersRes.json().get('username')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(sizeofReq)
        taskRow.append(name)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        allTasks.append(taskRow)

    with open("{}.csv".format(sizeofReq), "w") as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(allTasks)

    return 0


if __name__ == '__main__':
    export_to_CSV(int(argv[1]))
