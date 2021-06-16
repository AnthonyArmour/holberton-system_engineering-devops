#!/usr/bin/python3
"""returns information from  API"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    todo = 'https://jsonplaceholder.typicode.com/todos/'
    user = 'https://jsonplaceholder.typicode.com/users/'
    todo_dict = requests.get(todo).json()
    user_dict = requests.get(user).json()
    final_dic = {}
    task_dict = {}
    with open('todo_all_employees.json', 'w+') as jsonfile:
        for dic in user_dict:
            final_dic[dic["id"]] = []
            for d in todo_dict:
                if d["userId"] == dic["id"]:
                    username = dic["username"]
                    task_dict["username"] = username
                    task_dict["task"] = d["title"]
                    task_dict["completed"] = d["completed"]
                    final_dic[dic["id"]].append(dict(task_dict))
                    task_dict.clear()
        jsonfile.write(json.dumps(final_dic))
