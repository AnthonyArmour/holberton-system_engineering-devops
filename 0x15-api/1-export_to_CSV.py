#!/usr/bin/python3
"""returns information from  API"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    todo = 'https://jsonplaceholder.typicode.com/todos/'
    user = 'https://jsonplaceholder.typicode.com/users/'
    if len(argv) > 1:
        todo_dict = requests.get(todo, params={"userId": argv[1]}).json()
        user_dict = requests.get(user, params={"id": argv[1]}).json()
        EMPLOYEE_NAME = user_dict[0].get("name")
    row = []
    filecsv = str(argv[1]) + ".csv"
    with open(filecsv, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for dic in todo_dict:
            row.append(str(argv[1]))
            row.append(str(dic["username"]))
            row.append(str(dic["completed"]))
            row.append(str(dic["title"]))
            csvwriter.writerow(row)
            row.clear()
