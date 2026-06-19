import os
import tweepy
from gradio_client import Client

# 1. ask your Space for one tweet
space = Client("iloveworldpeace/tweetbot", token=os.environ["HF_TOKEN"])
tweet_text = space.predict(0.9, 1, api_name="/generate")
tweet_text = tweet_text.strip()[:280]                    # stay under X's limit

# 2. post it
try:
    me = client.get_me()
    print("Credentials OK. Logged in as:", me.data.username)
except Exception as e:
    print("get_me() failed:", repr(e))
    if getattr(e, "response", None) is not None:
        print("X response:", e.response.text)

try:
    client.create_tweet(text=tweet_text)
    print("Posted!")
except Exception as e:
    print("create_tweet failed:", repr(e))
    if getattr(e, "response", None) is not None:
        print("X response:", e.response.text)
