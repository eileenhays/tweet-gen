import os
from random import choice
import twitter


class Tweets(object):

	api = twitter.Api(
	                  consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
	                  consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
	                  access_token_key=os.environ.get("TWITTER_ACCESS_TOKEN_KEY"),
	                  access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
	                  )

	print api.VerifyCredentials()


	def __init__(self, screen_name=None):
		self.screen_name = screen_name


	def search_tweets(self):
	    """Search tweets given a screen_name."""

	    tweets = []
	    try:
		    statuses = api.GetUserTimeline(screen_name=self.screen_name, include_rts=False, count=200)
		    print statuses
	    except ValueError as error:
			print error
	    tweets.extend([s.text for s in statuses])

	    while len(statuses) != 0:
	    	try:
	    		print statuses[len(statuses)-1].id-1
	    		statuses = api.GetUserTimeline(screen_name=self.screen_name, include_rts=False, count=200, max_id=statuses[len(statuses)-1].id-1)
	    	except ValueError as error:
	    		print error
	    	tweets.extend([s.text for s in statuses])

	    return tweets


	@classmethod
	def make_starting_words_dict(tweet_data):
		"""Returns set of tuples of first two words of all tweets."""	

		starting_words = []

		for tweet in tweet_data:
			words = tweet.split()
			if len(words) >= 2:
				chain = (words[0], words[1])
				starting_words.append(chain)

		return starting_words


	@classmethod	
	def make_markov_dict(tweet_data):
	    """Takes tweet text as string; returns dictionary of markov chains."""

	    if tweet_data: 
		    markov_dict = {}

		    for tweet in tweet_data: 
			    words = tweet.split()

			    for i in range(len(words) - 2):
			    	first_word = words[i]
			    	second_word = words[i + 1]
			    	next_word = words[i + 2]

			        chain = (first_word, second_word)
			        value = next_word

			        markov_dict.setdefault(chain, []).append(value)

	    return markov_dict


	def random_tweet_generator(self):
	    """Returns random Markov tweet"""

	    tweets = search_tweets(self.screen_name)
	    starting_words = make_starting_words_dict(tweets)
	    markov_dict = make_markov_dict(tweets)
	    start = choice(starting_words)
	    text = [start[0], start[1]]
	    chain = start
		
	    while chain in markov_dict:
	        next_word = choice(markov_dict[chain])
	        text.append(next_word)
	        chain = (chain[1], next_word)

	    return " ".join(text)
