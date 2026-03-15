import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="web:runslick.monitor:v1.0"
)

subreddit = reddit.subreddit("running")

for submission in subreddit.new(limit=10):
    print(submission.title)
