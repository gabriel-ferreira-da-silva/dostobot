import time
import twitterkeys as keys
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime
import sys

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/var"

book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/assets/books/crime-and-punishment-english.txt"

book = BookHandler()
book.set_english_path(book_path)
book.last_update_date= datetime.now()

with open(file_path, 'wb') as file:
                # Serialize and write the variable to the file
                pickle.dump(book, file)
