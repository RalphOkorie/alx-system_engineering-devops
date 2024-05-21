#!/usr/bin/python3
"""Gather data from an API """
import requests
from sys import argv


def main():
    """Gather data from an API"""
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
