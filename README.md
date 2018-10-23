To Deploy you must have credstash access and run the deploy like this
```
TWITTER_CONSUMER_KEY=$(credstash -r us-west-2 get twitter.consumer_key) \
TWITTER_CONSUMER_SECRET=$(credstash -r us-west-2 get twitter.consumer_secret) \
TWITTER_ACCESS_KEY=$(credstash -r us-west-2 get twitter.access_token_key) \
TWITTER_ACCESS_SECRET=$(credstash -r us-west-2 get twitter.access_token_secret) \
ne sls deploy
```
