#!/usr/bin/python3
"""CSV file"""
import sys
import requests
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    name = user.get("username")
    work = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in work:
            user_data = [sys.argv[1], name, t.get("completed"), t.get("title")]
            writer.writerow(user_data)

