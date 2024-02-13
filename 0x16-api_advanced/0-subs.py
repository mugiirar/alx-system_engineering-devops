#!/usr/bin/python3
"""a function that queries the Reddit API
"""

import requests
import json
from sys import argv

def number_of_subscribers(subreddit):
    """finds number of subs"""
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent = "API-practice"

    request = requests.get(url, headers={'User-Agent': agent})

    if request.status_code != 200:
        return (0)

    else:
        jsons = request.json()
        count = jsons.get('data').get('subscribers')
        return count
