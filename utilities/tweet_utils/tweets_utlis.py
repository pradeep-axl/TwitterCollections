"""
Handles the tweets collection
"""
import csv
import logging
from datetime import date

import tweepy

from utilities.common_utils import generate_file_path, get_config


def create_twitter_api_connection():
    """
    A helper function to create the connection for twitter apis
    :rtype: object twitter API object
    """
    try:
        twitter_auth = tweepy.OAuthHandler(get_config("API_KEY"), get_config("API_SECRET_KEY"))
        twitter_auth.set_access_token(get_config("ACCESS_TOKEN"), get_config("ACCESS_TOKEN_SECRET"))
        return tweepy.API(twitter_auth)
    except tweepy.TweepError as tweepy_error:
        logging.error(f"Error while making twitter API connection : {tweepy_error.api_code} {tweepy_error.reason}")


def get_user_timeline_tweets(twitter_user_handle: str, fetch_max=0):
    """
    Fetches user time line tweets,using user handle
    :param twitter_user_handle:
    :param fetch_max: int maximum number of tweets to fetch
    """
    # Create Twitter connection
    twitter_api = create_twitter_api_connection()
    # initialize a list to hold all the Tweets on user profile
    all_tweets = []

    # initial request tweets
    first_api_call = True
    # Creating the condition to fetch with a limit and without the limit i.e fetch_max or all_tweets
    condition = True
    last_tweet = ""
    while condition:
        logging.info(f" For {twitter_user_handle} getting tweets before {last_tweet}")
        # Using last_tweet as max_id to get the further tweet and preventing duplicates

        if first_api_call:
            # Don't pass the max_id for first api request
            new_tweets = twitter_api.user_timeline(screen_name=twitter_user_handle, count=200)
            first_api_call = False
        else:
            new_tweets = twitter_api.user_timeline(screen_name=twitter_user_handle, count=200, max_id=last_tweet)

        all_tweets.extend(new_tweets)
        last_tweet = all_tweets[-1].id - 1
        logging.info(f"{twitter_user_handle} ...{len(all_tweets)} tweets downloaded so far")
        condition = (len(new_tweets) > 0) & (len(all_tweets) <= fetch_max) if fetch_max else (len(new_tweets) > 0)

    # Save the data in csv with following keys.
    save_tweets = [[tweet.id_str, tweet.created_at, tweet.text, tweet.favorite_count, tweet.in_reply_to_screen_name,
                    tweet.retweeted] for tweet in all_tweets]
    # write the csv
    with open(generate_file_path("output", f'{twitter_user_handle}_tweets-{date.today()}.csv'), 'w',
              encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text", "likes", "in reply to", "retweeted"])
        writer.writerows(save_tweets)
