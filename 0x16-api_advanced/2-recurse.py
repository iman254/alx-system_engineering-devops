#!/usr/bin/python3
"""recursive function that returns a list containing titles
of a hot article for a subreddit"""

import requests


def recurse(subreddit, after=None, hot_list=[]):
    """list containing titles of all the hot articles for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(subreddit, after)
    headers = {"User-agent": 'my agent'}
    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
