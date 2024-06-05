#!/usr/bin/python3
""" Get all posts recursively """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Get all posts recursively """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Ayo User Agent 1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get('data').get('children')
    hot_list = hot_list or []
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = response.json()["data"]["after"]
    return hot_list if after is None else recurse(subreddit, hot_list, after)
