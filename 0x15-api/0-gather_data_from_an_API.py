#!/usr/bin/python3
"""
a Python script that, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/todos')
    EMPLOYEE = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/'
                            )
    EMPLOYEE_NAME = EMPLOYEE.json().get("name")
    NUMBER_OF_DONE_TASKS = len([item
                               for item in r.json() if item.get("completed")])
    TASK_TITLE = [item.get("title")
                  for item in r.json() if item.get("completed")]
    TOTAL_NUMBER_OF_TASKS = len(r.json())

    print(f"Employee {EMPLOYEE_NAME} is done with "
          f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    [print(f"\t {item}") for item in TASK_TITLE]
