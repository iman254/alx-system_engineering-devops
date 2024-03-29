#!/usr/bin/python3
"""A python function that querries reddit api
and returns no of subs for a given subredit"""

import requests


def number_of_subscribers(subreddit):
    """returns the num of subs in a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        no_subs = data.get("data").get("subscribers")
        return no_subs
    else:
        return 0
