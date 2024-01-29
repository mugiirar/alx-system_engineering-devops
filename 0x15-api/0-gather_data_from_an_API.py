#!/usr/bin/python3
"""listing information"""
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    work = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []

    for k in work:
        if k.get("completed") is True:
            completed.append(k.get("title"))


    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(work)))

    for com in completed:
        print("\t {}".format(com))
