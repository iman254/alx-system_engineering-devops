#!/usr/bun/python3
"""function that prints top 10 hot posts from subredditt
"""

import requests


def top_ten(subreddit):
    """Gets hot top 10 posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
