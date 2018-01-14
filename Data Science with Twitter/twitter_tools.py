import tweepy
import json
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

class TwitterStreamListener(tweepy.StreamListener):
	def __init__(self, api=None):
		super(TwitterStreamListener, self).__init__()
		self.num_tweets = 0
		#self.file = open("tweets"+today+".txt", "w")
		self.file = open("tweets.txt", "w")

	def on_status(self, status):
		tweet = status._json
		self.file.write( json.dumps(tweet) + '\n' )
		self.num_tweets += 1
		if self.num_tweets < 10000:
		    return True
		else:
		    return False
		self.file.close()

	def on_error(self, status):
		print(status)

class TwitterAuth():
	def __init__(self):
		self.type = 'authenticator'

	def authenticate(self, filename):
		self.filename = filename
		with open(filename) as file:
			self.access_token = file.readline().split()[2]
			self.access_token_secret = file.readline().split()[2]
			self.consumer_key = file.readline().split()[2]
			self.consumer_secret = file.readline().split()[2]
		print('Keys Retrieved')

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)
		print('Authenticated')	
