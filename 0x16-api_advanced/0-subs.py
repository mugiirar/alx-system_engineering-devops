#!/usr/bin/python3

import requests
from sys import argv
import json

def number_of_subscribers(subreddit):

    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent = "API-practice"

    request = requests.get(url, headers={'User-Agent': agent})

    if request.status_code != 200:
        return (0)

    else:
        jsons = request.json()
        count = jsons.get('data').get('subscribers')
        return count
