# this program tweets then replys to a tweet

import twitterkeys as keys
import tweepy


client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

f = open('portugues', 'r', encoding="utf-16")
tt = f.readlines()
f.close()
t=""
for s in tt:
    t+=s
print(t)
t+="hell twiit"
res=client.create_tweet(text=t)

f = open('portugues', 'r', encoding="utf-16")
tt = f.readlines()
f.close()
t=""
for s in tt:
    t+=s
t+=",again"
res_id = res[0]['id']
res=client.create_tweet(text=t, in_reply_to_tweet_id= res_id)

print(res[0]['id'])

