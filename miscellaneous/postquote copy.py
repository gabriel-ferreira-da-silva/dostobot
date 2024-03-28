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
last_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/lb"

book=None
last_book=None
with open(file_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        bookarr = pickle.load(file)

with open(last_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        last_book = pickle.load(file)



index = random.randint(0, len(bookarr) -1)
book = bookarr[index]
book.getnextquote()
quote = book.en_book.current_quote
book.en_book.last_update_date = datetime.now()


last_book = book
bookarr[index] = book

with open(file_path, 'wb') as file:
        # Deserialize and retrieve the variable from the file
        pickle.dump(bookarr,file)

with open(last_path, 'wb') as file:
        # Deserialize and retrieve the variable from the file
        pickle.dump(last_book, file)

quotes=[]

print(quote)

q=quote[0:240]
quotes.append(q)
quote = quote[240:]
print("quote size "+ str(len(quote)))

res= client.create_tweet(text=q)
res_id = res[0]['id']

while len(quote) > 0:
        q1=quote[0:240]
        quotes.append(q1)
        quote = quote[240:]
        print("quote size " + str(len(quote)))
        time.sleep(2)
        res= client.create_tweet(text=q1, in_reply_to_tweet_id=res_id)
        res_id = res[0]['id']
        print(res)


status = ""
status += book.en_book.book_title + "; "
status += "Chapter " + book.en_book.current_chapter[7:]+ ", " 
status += "Part " + book.en_book.current_part[5:]+"."

res= client.create_tweet(text=status, in_reply_to_tweet_id=res_id)

print("\n\n")
book.status()