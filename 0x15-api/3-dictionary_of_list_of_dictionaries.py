#!/usr/bin/python3
"""fetching json data from an api"""

import json
import requests


if __name__ == "__main__":
    emp_url = "https://jsonplaceholder.typicode.com/users/"
    emp_dict = requests.get(emp_url).json()
    file_name = "todo_all_employees.json"
    my_dict = {}

    for elem in emp_dict:
        name = elem.get("username")
        emp_id = str(elem.get("id"))
        emp_data = requests.get("{}{}/todos".format(emp_url, emp_id))
        emp_data = emp_data.json()
        my_dict[emp_id] = []
        for item in emp_data:
            inter_dict = {}
            inter_dict["username"] = name
            inter_dict["task"] = item.get("title")
            inter_dict["completed"] = item.get("completed")
            my_dict[emp_id].append(inter_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
