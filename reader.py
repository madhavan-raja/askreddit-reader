import praw
import json
import random

creds = json.load(open("credentials.json"))

LIMIT = 100


def get_content():
    reddit = praw.Reddit(client_id=creds['client_id'], client_secret=creds['client_secret'], username=creds['username'], password=creds['password'], user_agent=creds['user_agent'])
    sub = reddit.subreddit('AskReddit')
    sub_hot = sub.hot(limit=LIMIT)

    random_sub = random.choice(list(sub_hot))
    random_sub.comments.replace_more(limit=None)
    random_comment = random.choice(list(random_sub.comments))

    return f"[u/{random_sub.author.name}]: {random_sub.title}", f"[u/{random_comment.author.name}]: {random_comment.body}"
    