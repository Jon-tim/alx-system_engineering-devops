#!/usr/bin/python3
"""
PROGRAM:
    A function that queries the Reddit API & returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

HINT:
    No authentication is necessary for most features of the Reddit API.
    If you’re getting errors related to Too Many Requests,
    ensure you’re setting a custom User-Agent.

REQUIREMENTS:
    Prototype:
        def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.

NOTE:
    Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
"""

import requests

# if __name__ == "__main__":
def number_of_subscribers(subreddit):
    """main function"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # print(response.json())
    if response.status_code == 200:
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return (subscribers_count)
        # elif response.status_code in [301, 302, 307, 308]:
        #     print(0)
    else:
        # print(f"Error: {response.status_code} - {response.text}")
        return (0)
