import json

import sys
sys.path.append('vendor')

import markovify
import twitter

from credstash import getSecret

def read_corpus():
    """Read corpus.txt to prime responses."""
    with open("corpus.txt") as f:
        text = f.read()

    return markovify.Text(text)


def send_tweet(message):
    """Send a tweet to the twitter account."""
    consumer_key = getSecret('twitter.consumer_key')
    consumer_secret = getSecret('twitter.consumer_secret')
    access_token_key = getSecret('twitter.access_token_key')
    access_token_secret = getSecret('twitter.access_token_secret')

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    response = api.PostUpdate(message)
    print(response)


def make_tweet(event, context):
    text_model = read_corpus()
    print(text_model.make_short_sentence(140))

