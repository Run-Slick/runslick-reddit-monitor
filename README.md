# Run Slick Reddit Monitor

This project is an internal monitoring tool that uses the Reddit Data API to identify public discussions related to running, endurance sports, and common athlete issues such as chafing, hot spots, blisters, and gear friction.

The application scans a limited number of relevant subreddits and identifies discussions where users are asking for advice or sharing experiences related to endurance sports.

The purpose of the tool is to help the account holder discover discussions and participate in the community where appropriate by sharing knowledge and personal experience.

The application:

- Uses the official Reddit Data API via PRAW
- Reads publicly available Reddit posts and comments
- Collects minimal metadata such as post title, URL, subreddit, and timestamp
- Stores results locally for review

The tool does **not automatically post comments or messages**. All participation on Reddit is performed manually by the account holder.

## Technology

- Python
- PRAW (Python Reddit API Wrapper)
- SQLite / CSV storage

## Example functionality

- Monitor running-related subreddits
- Identify discussions about chafing and anti-friction products
- Surface relevant threads for manual review

## Reddit API

This project uses the official Reddit Data API via the PRAW library.

https://github.com/praw-dev/praw
