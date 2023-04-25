#!/usr/bin/python3
"""fetching json data from an api"""

import requests
import json
from sys import argv
import csv


if __name__ == "__main__":
    emp_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/" + emp_id
    emp_dict = requests.get(emp_url).json()
    emp_name = emp_dict.get("username")
    emp_todo = requests.get("{}/todos".format(emp_url))
    emp_todo = emp_todo.json()
    file_name = emp_id + ".json"
    my_dict = {}

    my_dict[emp_id] = []

    for elem in emp_todo:
        inter_dict = {}
        inter_dict["task"] = elem.get("title")
        inter_dict["completed"] = elem.get("completed")
        inter_dict["username"] = emp_name
        my_dict.get(emp_id).append(inter_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
