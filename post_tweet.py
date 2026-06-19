import os
import tweepy
from gradio_client import Client

# 1. ask your Space for one tweet
space = Client("iloveworldpeace/tweetbot", token=os.environ["HF_TOKEN"])
tweet_text = space.predict(0.9, 1, api_name="/generate")
tweet_text = tweet_text.strip()[:280]                    # stay under X's limit

print(Client.get_me())

# 2. post it
client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_SECRET"],
)
client.create_tweet(text=tweet_text)
print("Posted:", tweet_text)
