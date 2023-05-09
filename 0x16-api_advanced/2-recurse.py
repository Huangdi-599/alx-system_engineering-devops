#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if data is None:
        return None
    children = data.get('children')
    if children is None or len(children) == 0:
        return hot_list
    for child in children:
        title = child.get('data').get('title')
        hot_list.append(title)
    after = data.get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
