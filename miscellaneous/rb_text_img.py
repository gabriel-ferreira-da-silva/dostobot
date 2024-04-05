# this program tweets a image with text

import twitterkeys as keys
import tweepy


client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)


media = api.media_upload("rodion.jpg")
res=client.create_tweet(text="he is so cute!", media_ids=[media.media_id])
print(res)