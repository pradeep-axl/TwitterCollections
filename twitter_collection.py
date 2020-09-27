"""
Contains code to collect tweets
"""
import os
import logging
import logging.config
import time

from utilities.tweet_utils.tweets_utlis import get_user_timeline_tweets
from utilities.common_utils import generate_file_path, load_text_file


def main():
    start = time.time()
    # logging configurations logic
    log_info = os.getenv("LOG_INFO", default=logging.INFO)
    log_file_path = generate_file_path("log", "twitter_collection.log")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    logging.basicConfig(filename=log_file_path, level=log_info,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt="%Y-%m-%dT%H:%M:%S%z",
                        filemode='a')

    logging.info("Twitter data collection process started")

    # get the path of twitter handle file
    input_file_path = generate_file_path("inputs", "twitter_user_handle.txt")
    twitter_user_handles_list = load_text_file(input_file_path)

    if len(twitter_user_handles_list) > 0:
        for user_handle in twitter_user_handles_list:
            get_user_timeline_tweets(user_handle.rstrip(), fetch_max=1000)
    else:
        logging.warning("No user handles specified in input file")
    logging.info(f'Twitter data collection process ended: Execution time: {time.time() - start}')


if __name__ == '__main__':
    main()
