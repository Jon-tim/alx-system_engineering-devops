#!/usr/bin/python3
"""
a Python script that export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/todos')
    USER = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/'
                        )
    USER_ID = USER.json().get("id")
    USERNAME = USER.json().get("username")

    data = [
        [USER_ID, USERNAME, item.get("completed"), item.get("title")]
        for item in r.json()
    ]

    with open(f"{USER_ID}.csv", 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
