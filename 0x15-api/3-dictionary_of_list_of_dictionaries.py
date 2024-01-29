#!/usr/bin/python3
"""Contains a Python script that, using the JSONplaceholder API, for a given
employee ID, returns all tasks from all employees, in JSON format"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    users_data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    all_tasks = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    employee_tasks_dict = {}
    username_dict = {}

    # Create dictionaries for employee tasks and usernames
    for user in users_data:
        employee_id = user.get("id")
        employee_tasks_dict[employee_id] = []
        username_dict[employee_id] = user.get('username')

    # Populate the employee tasks dictionary with task details
    for task in all_tasks:
        task_details = {}
        employee_id = task.get('userId')
        task_details["task"] = task.get('title')
        task_details["completed"] = task.get('completed')
        task_details["username"] = username_dict.get(employee_id)
        employee_tasks_dict.get(employee_id).append(task_details)

    # Write the results to a JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(employee_tasks_dict, json_file)

