#!/usr/bin/python3
"""Gather data from an API and export to list of dictionaries"""

import json
import requests
from sys import argv


def main():
    """Gather data from an API and export to list of dictionaries"""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    data = {}
    for user in users:
        data[user.get('id')] = [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in todo if task.get('userId') == user.get('id')]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
