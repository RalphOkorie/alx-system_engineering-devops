#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
from sys import argv


def main():
    """Gather data from an API and export to CSV"""
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get('username'),
                            task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
