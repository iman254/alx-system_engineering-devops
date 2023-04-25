#!/usr/bin/python3
"""script that using this REST API, for a given employee ID,
   returns information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/" + emp_id
    emp_dict = requests.get(emp_url).json()
    emp_name = emp_dict.get("name")
    emp_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    emp_todo = emp_todo.json()
    total_todo = 0
    titles_completed = []
    number_completed = 0

    for item in emp_todo:
        if item.get("userId") == int(emp_id):
            total_todo += 1
            if item.get("completed") is True:
                number_completed += 1
                titles_completed.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, number_completed, total_todo))
    for title in titles_completed:
        print("\t {}".format(title))
