import tweepy
import json
import datetime
import pandas as pd
import json
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import time

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

class TwitterStreamListener(tweepy.StreamListener):
	def __init__(self, api=None):
		super(TwitterStreamListener, self).__init__()
		self.num_tweets = 0
		#self.file = open("tweets"+today+".txt", "w")
		self.file = open("tweets_data/tweets.txt", "w")

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


class TweetsPreprocessing():
	def __init__(self):
		self.type = 'class'
		
	def preprocess(self, filepath):
		tweets_data = []
		
		try:
			#-------- Reading Tweets data from file --------------
			with open(filepath,'r') as file:
				for line in file:
					tweet = json.loads(line)
					tweets_data.append(tweet)
			print('========== tweets imported ============')		
			print(tweets_data[0].keys())
			
			#Create dataframe using only text keys from tweets json data
			df = pd.DataFrame(tweets_data, columns=['text'])
			print('\n========== dataframe created ============')
			
			
			#-------- Begin preprocessing ----------		
			#preprocess text
			t0 = time.time()
			print('\nBegin Preprocessing')		
			df['text'] = df['text'].apply(lambda x: self.preprocess_text(x))
			
			print('\nPreprocessing concluded on ',time.time()-t0,'s')
			print(df.head())
			
			df.to_csv('clean_tweets.txt', index=False)
				
		except:
			print('unexpected error')
	
	
	def preprocess_text(self, text):
		'''
		What will be covered:
		1. Remove 'RT', '\n'
		2. Remove Username
		3. Remove punctuation
		4. Stem the words
		5. Remove stopwords
		6. Return list of clean text words
		'''			
		
		#String format of username e.g @bisha, this kind of word will be removed
		pattern = re.compile('\@\S+\:')
		
		#stemmer factory
		factory = StemmerFactory()
		stemmer = factory.create_stemmer()
		
		#1
		text = text.replace('RT ','')
		text = text.replace('\n',' ')
		
		#2
		text = [word for word in text.split() if bool(pattern.match(word))==False]
		
		#3
		nopunc = [word for word in text if word.lower() not in string.punctuation]
		text = ' '.join(nopunc)
		
		#4
		stemmed = stemmer.stem(text)
		
		#5
		
		
		#6
		return stemmed
