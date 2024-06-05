#!/usr/bin/python3
""" Get all posts recursively and count words """

import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """ Get all posts recursively and count words

    Args:
        subreddit (str): subreddit to search
        word_list (list): words to search for
        after (str, optional): pagination. Defaults to None.
        word_counts (int, optional): word counts. Defaults to None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Ayo User Agent 1.0'}
    params = {'limit': 100}
    # if there is an after, next page, add it to the params dict
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    # get all posts from the response
    posts = response.json().get('data').get('children')
    # initialize word_counts dict if it doesn't exist
    word_counts = word_counts or {}
    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower():
                # get the value of the key, if it doesn't exist, return 0
                word_counts[word.lower()] = word_counts.get(
                    word.lower(), 0) + 1
    after = response.json()["data"]["after"]
    # if end of pagination and word_counts is empty, print nothing and return
    if after is None:
        if not word_counts:
            return
        # sort the word_counts dict by value in desc, then key in asc order
        for key, value in sorted(word_counts.items(), key=lambda x: (-x[1],
                                                                     x[0])):
            print("{}: {}".format(key.lower(), value))
        return
    return count_words(subreddit, word_list, after, word_counts)
