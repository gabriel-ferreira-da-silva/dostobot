import time
import twitterkeys as keys
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)



file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/var"

while 1:
    try:
        bh= BookHandler()
        with open(file_path, 'rb') as file:
            # Deserialize and retrieve the variable from the file
            bh = pickle.load(file)
    
        delta = datetime.now()-bh.last_update_date
        if delta.total_seconds() > 180:
            bh.getnextquote()
            bh.status()
            
            bh.last_update_date = datetime.now()

            with open(file_path, 'wb') as file:
                # Serialize and write the variable to the file
                pickle.dump(bh, file)
                
            quote = bh.en_book.current_quote[0:280]
            res=client.create_tweet(text= quote)
            print(res)
    except:
        print("something wrong happened!")
        print("now sleep for 10 secs")
        time.sleep(10)


