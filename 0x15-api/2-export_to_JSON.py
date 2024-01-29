#!/usr/bin/python3
"""json export"""
import json
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    name = user.get("name")
    work = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        json.dump({sys.argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name
            } for t in work]}, jsonfile)

