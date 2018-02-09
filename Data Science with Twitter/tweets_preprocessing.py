from twitter_tools import TweetsPreprocessing

input_file  = 'tweets_data/tweets2018-01-14_hujan.txt'

process_tweets = TweetsPreprocessing()
process_tweets.preprocess(input_file)