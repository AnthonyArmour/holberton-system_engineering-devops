#!/usr/bin/python3
"""returns information from API"""

if __name__ == "__main__":
    from sys import argv
    import requests
    todo = 'https://jsonplaceholder.typicode.com/todos/'
    user = 'https://jsonplaceholder.typicode.com/users/'
    if len(argv) > 1:
        todo_dict = requests.get(todo, params={"userId": argv[1]}).json()
        user_dict = requests.get(user, params={"id": argv[1]}).json()
        username = user_dict[0].get("name")
    num_of_tasks = len(todo_dict)
    done_tasks = 0
    for dic in todo_dict:
        if dic["completed"] is True:
            done_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(username, done_tasks, num_of_tasks))
    for dic in todo_dict:
        if dic["completed"] is True:
            print("\t{}".format(dic["title"]))
