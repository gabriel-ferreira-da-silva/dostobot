
# this program is to discover how the fuck i
# print fucking cyrilic characters in a tweet

import twitterkeys as keys
import tweepy


client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

f = open('russo', 'r', encoding="utf-8")
tt = f.readlines()
f.close()

t=""
for s in tt:
    t+=s

tt = t.encode('utf-8')
str = tt.decode("utf-8")
client.create_tweet(text= str, in_reply_to_tweet_id=1759397780169036225)

