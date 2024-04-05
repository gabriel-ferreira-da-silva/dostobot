import random
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

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"

book=None
with open(file_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        bookarr = pickle.load(file)

index = random.randint(0, len(bookarr) -1)
book = bookarr[index]
book.getnextquote()
quote = book.en_book.current_quote
book.en_book.last_update_date = datetime.now()


bookarr[index] = book

with open(file_path, 'wb') as file:
        # Deserialize and retrieve the variable from the file
        pickle.dump(bookarr,file)

quotes=[]

print(quote)

q=quote[0:240]
quotes.append(q)
quote = quote[240:]

while len(quote) > 240:
        q1=quote[0:240]
        quotes.append(q1)
        quote = quote[240:]


res= client.create_tweet(text=quotes[0])
res_id = res[0]['id']
for i in range(1, len(quotes)):
        res= client.create_tweet(text=quotes[i], in_reply_to_tweet_id=res_id)
        res_id = res[0]['id']
        print(res)

status = ""
status += book.en_book.book_title + "\n"
status += book.en_book.current_chapter + ", " 
status += book.en_book.current_part

res= client.create_tweet(text=status, in_reply_to_tweet_id=res_id)

print("\n\n")
book.status()