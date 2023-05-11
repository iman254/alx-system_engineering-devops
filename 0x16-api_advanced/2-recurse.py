#!/usr/bin/python3
"""recursive function that returns a list containing titles
of a hot article for a subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """list containing titles of all the hot articles for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(subreddit, after)
    header = {"User-agent", 'my agent'}
    post = request.get(url, headeers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = post.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hotlist)
    else:
        return (None)
