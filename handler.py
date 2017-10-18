import json

import os
import sys
sys.path.append('vendor')

import markovify
import twitter


def read_corpus():
    """Read corpus.txt to prime responses."""
    with open("corpus.txt") as f:
        text = f.read()

    return markovify.Text(text)


def send_tweet(message):
    """Send a tweet to the twitter account."""
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token_key = os.environ['TWITTER_ACCESS_KEY']
    access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    response = api.PostUpdate(message)
    print(response)


def make_tweet(event, context):
    text_model = read_corpus()
    tweet = text_model.make_short_sentence(140)
    send_tweet(tweet)
