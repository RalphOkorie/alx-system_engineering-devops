#!/usr/bin/python3
""" Get subreddit subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Get number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Ayo User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
