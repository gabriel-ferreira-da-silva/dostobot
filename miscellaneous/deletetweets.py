import time
import twitterkeys as keys
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


screen_name ="dostobot_"
user = client.get_user(username=screen_name)

print(user)
my_id = user.id_str
print(my_id)
#res = client.get_users_tweets(my_id)
#print("\n\n\n")
#print(res)