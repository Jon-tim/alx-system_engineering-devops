#!/usr/bin/python3
"""
a Python script that export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/todos')
    USER = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/')
    USER_ID = USER.json().get("id")
    USERNAME = USER.json().get("username")

    dictionary = {USER_ID: [{"task": item.get("title"),
                             "completed": item.get("completed"),
                             "username": USERNAME} for item in r.json()
                            ]}
    with open(f"{USER_ID}.json", "w") as file:
        json.dump(dictionary, file)
