#!/usr/bin/python3
"""returns information from  API"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    todo = 'https://jsonplaceholder.typicode.com/todos/'
    user = 'https://jsonplaceholder.typicode.com/users/'
    if len(argv) > 1:
        todo_dict = requests.get(todo, params={"userId": argv[1]}).json()
        user_dict = requests.get(user, params={"id": argv[1]}).json()
        username = user_dict[0].get("username")
    lst = []
    task_dict = {}
    filejson = str(argv[1]) + ".json"
    with open(filejson, 'w+') as jsonfile:
        for dic in todo_dict:
            task_dict["task"] = dic["title"]
            task_dict["completed"] = dic["completed"]
            task_dict["username"] = username
            lst.append(dict(task_dict))
            task_dict.clear()
        dic = {argv[1]: lst}
        jsonfile.write(json.dumps(dic))
