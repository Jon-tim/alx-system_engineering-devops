#!/usr/bin/python3
"""
a Python script that export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER = requests.get('https://jsonplaceholder.typicode.com/users/').json()

    dictionary = {}

    for user in USER:
        username = user.get("username")
        uid = user.get("id")
        r = requests.get(f'{url}users/{uid}/todos').json()

        data = [{
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in r]

        dictionary[uid] = data

    with open("todo_all_employees.json", "w") as file:
        json.dump(dictionary, file)
