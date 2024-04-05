import random
import time
import sys
sys.path.insert(0, 'C:/Users/gab_f/OneDrive/Desktop/')
import twitterkeys as keys
import tweepy
import pickle
from bookhandler import BookHandler
import datetime

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"
last_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/lb"

suc_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/sucess.txt"

book=None
last_book=None

with open(last_path, 'rb') as file:
        last_book = pickle.load(file)

with open(file_path, 'rb') as file:
        bookarr = pickle.load(file)

index = random.randint(0, len(bookarr)-1)
book = bookarr[index]
book.getnextquote()
quote = book.en_book.current_quote
book.en_book.last_update_date = datetime.datetime.now()
npost=0
deltatime=3

if last_book !=None:        
        datedif= abs(last_book.en_book.last_update_date - book.en_book.last_update_date)
        datedif = datedif.seconds
        datedif = datedif / (3600)
        print("\nlastbook: " +str(last_book.en_book.last_update_date) )
        print("\nbook: " +str(book.en_book.last_update_date) )
        print("\n\ntime diference "+ str(datedif)+"\n\n")
        if datedif < 4:
                print("\n\n\nExiting program on post time dif")
                npost=-100000000000

        while datedif >= deltatime and npost > -1:
                datedif = datedif - deltatime
                npost+=1
else:
        npost=1


while npost >= 1:
        time.sleep(2)
        npost-=1

        with open(file_path, 'rb') as file:
                bookarr = pickle.load(file)

        index = random.randint(0, len(bookarr) -1)
        book = bookarr[index]
        book.getnextquote()
        quote = book.en_book.current_quote
        book.en_book.last_update_date = datetime.datetime.now()

        if book.en_book.current_pos >= (len(book.en_book.book_text) - 100):
                book.en_book.current_pos = 0
                book.en_book.current_part="part 1"
                book.en_book.current_chapter="chapter 1"
                
        bookarr[index] = book

        with open(file_path, 'wb') as file:
                pickle.dump(bookarr,file)

        postquote=""
        res=None
        res_id=None

        for ch in quote:
                if ch==" " and len(postquote) > 250:
                        postquote+=" +"
                        res= client.create_tweet(text=postquote, in_reply_to_tweet_id=res_id)
                        res_id = res[0]['id']
                        postquote=""
                
                postquote+=ch

        res= client.create_tweet(text=postquote, in_reply_to_tweet_id=res_id)
        res_id = res[0]['id']

        status = ""
        status += book.en_book.book_title + ".\n"
        status += "Chapter " + book.en_book.current_chapter[7:]+ ", " 
        status += "Part " + book.en_book.current_part[5:]+"."

        res= client.create_tweet(text=status, in_reply_to_tweet_id=res_id)

        print("\n\n")
        book.status()

        last_book = book
        with open(last_path, 'wb') as file:
                pickle.dump(last_book, file)

