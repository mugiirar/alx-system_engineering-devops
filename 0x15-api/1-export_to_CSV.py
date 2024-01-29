#!/usr/bin/python3
""" Contains a python script that, using the JSONplaceholder API, for a given
    employee ID, returns information about employees todo list progress """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    # todo variable = grabs all todos (completed or not) for the user passed in
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    with open("{}.csv".format(userId), 'w') as acsvfile:
        csvwriter = csv.writer(acsvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([userId, name.get('username'),
                                task.get('completed'), task.get('title')])
