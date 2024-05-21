#!/usr/bin/python3
"""Gather data from an API and export to JSON"""

import json
import requests
from sys import argv


def main():
    """Gather data from an API and export to JSON"""
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        } for task in todo]}, jsonfile)


if __name__ == "__main__":
    main()
