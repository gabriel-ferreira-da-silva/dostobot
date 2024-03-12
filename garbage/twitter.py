import tweepy

api_key = "jc5VtR1prNSgc8PjVZwpP4Npu"
api_secret = "RdpciOfdk7IraHX0QJTr4h6rwriJfYrWw7W4cms3OYHspaBr1z"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAFoorQEAAAAAN7cxhmI3VCArNgZGmSp24QrN%2Fao%3DvugLb4L3ltxel7ApV4qr7ZEfgr06aINonOMFJsMjRjJmqmH6Pe"
access_token = "1611874632050638848-Bwoz253M0igDnL3T55lPnuUua6aQhs"
access_token_secret = "OWlvx4MSD2lXr80zeTy7V8QVpn6r1JXvX2KUEzwdYY0v0"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

f = open('crime-and-punishment.txt', 'r', encoding="utf-8")

tt = f.readlines()
f.close()
t=""
for i in range(10,14):
    t+=tt[i]
client.create_tweet(text=t)

print("tweet made!")