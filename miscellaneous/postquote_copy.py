import time
import sys
sys.path.insert(0, 'C:/Users/gab_f/OneDrive/Desktop/')
import twitterkeys as keys
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/var"

book=None
with open(file_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        book = pickle.load(file)

book.getnextquote()
quote = book.en_book.current_quote

with open(file_path, 'wb') as file:
        # Deserialize and retrieve the variable from the file
        pickle.dump(book,file)
print(quote)

res= client.create_tweet(text=quote)
print(res)

print("\n\n")
book.status()