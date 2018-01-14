import tweepy
from twitter_tools import TwitterStreamListener

with open('twitter_api_key.txt','r') as file:
	access_token = file.readline().split()[1]
	access_token_secret = file.readline().split()[1]
	consumer_key = file.readline().split()[1]
	consumer_secret = file.readline().split()[1]

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	print('Authenticated')
	
l = TwitterStreamListener()

stream = tweepy.Stream(auth, l)
stream.filter(track=[], locations=[94.969833,-11.00485,141.021805,6.07573])
