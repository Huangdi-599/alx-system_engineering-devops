#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns the number of
subscribers for a given subreddit
"""
import requests


def count_words(subreddit, word_list, count_dict={}, after=None):
    """
    Prints a sorted count of given keywords (case-insensitive) in the
    subreddit's hot articles
    """
    if after is None:
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
        count_dict = {word.lower(): 0 for word in word_list}
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data')
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            count_dict[word] += title.count(word.lower())
    after = data.get('after')
    if after is None:
        sorted_words = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print('{}: {}'.format(word, count))
    else:
        count_words(subreddit, word_list, count_dict, after)
