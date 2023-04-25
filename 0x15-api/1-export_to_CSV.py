#!/usr/bin/python3
"""fetching json data from an api"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/" + emp_id
    emp_dict = requests.get(emp_url).json()
    emp_name = emp_dict.get("username")
    emp_todo = requests.get("{}/todos".format(emp_url))
    emp_todo = emp_todo.json()
    file_name = emp_id + ".csv"

    with open(file_name, 'w') as csvfile:
        for item in emp_todo:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), emp_name, item.get("completed"),
                item.get("title")))
