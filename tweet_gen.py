import os
import twitter
import string
import sys
from random import choice
from flask import session
from ast import literal_eval as make_tuple

reload(sys)
sys.setdefaultencoding("utf-8")


class UserTweets(object):
	"""Tweets from a user to create new Markov chain Tweets."""

	api = twitter.Api(consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
	                  consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
	                  access_token_key=os.environ.get("TWITTER_ACCESS_TOKEN_KEY"),
	                  access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
	                  )

	print api.VerifyCredentials()

	def __init__(self, screen_name=None):
		"""Initiates a Twitter screen name object"""

		self.screen_name = screen_name
		tweet_data = self.search_tweets()
		self.start_lst = self.make_starting_lst(tweet_data)
		self.markov_dict = self.make_markov_dict(tweet_data)


	def __repr__(self):
		return "<UserTweets for %s>" % (self.screen_name) 


	def search_tweets(self):
	    """Search tweets given a screen_name."""

	    tweets = []
	    try:
		    statuses = UserTweets.api.GetUserTimeline(screen_name=self.screen_name, 
		    										  include_rts=False, 
		    										  count=200
		    										  )
		    print statuses
	    except ValueError as error:
			print error
	    tweets.extend([s.text for s in statuses])

	    while len(statuses) != 0:
	    	try:
	    		print statuses[len(statuses)-1].id-1
	    		statuses = UserTweets.api.GetUserTimeline(screen_name=self.screen_name, 
	    												  include_rts=False, 
	    												  count=200, 
	    												  max_id=statuses[len(statuses)-1].id-1)
	    	except ValueError as error:
	    		print error
	    	tweets.extend([s.text for s in statuses])

	    return tweets


	def make_starting_lst(self, tweet_data):
		"""Returns list of tuples of first two words of all tweets."""	

		starting_words = []

		for tweet in tweet_data:
			tweet = self.strip_punctuation(tweet).encode("utf-8")
			words = tweet.split()
			if len(words) >= 2:
				first_word = self.scrub(words[0])
				second_word = self.scrub(words[1])
				chain = str((first_word, second_word))

				starting_words.append(chain)

		return starting_words


	def make_markov_dict(self, tweet_data):
	    """Takes tweet text as string; returns dictionary of markov chains."""

	    if tweet_data: 
		    markov_dict = {}

		    for tweet in tweet_data: 
		    	tweet = self.strip_punctuation(tweet).encode("utf-8")
		    	words = tweet.split()
		    	for i in range(len(words) - 2):
		    		first_word = self.scrub(words[i])
		    		second_word = self.scrub(words[i + 1])
		    		next_word = self.scrub(words[i + 2])
			        chain = str((first_word, second_word))
			        value = next_word
 
			        markov_dict.setdefault(chain, []).append(value)

	    return markov_dict


	@staticmethod
	def strip_punctuation(words):
		"""Removes punctuation from string."""

		exclude = set('!"\()./:;<=>?[\\]^_`{|}~')
		strip_words = ''.join(ch for ch in words if ch not in exclude)

		return strip_words


	@staticmethod
	def scrub(word):
		"""Removes words that start with '@', 'http', or 'via' from chains."""

		if ("@" == word[0]) or("http" in word) or ("via" == word):
			return ""

		return word


	def random_tweet_generator(self):
	    """Returns random Markov tweet and saves to session"""

	    start = make_tuple(choice(self.start_lst))
	    chain = start
	    text = [chain[0], chain[1]]

	    while str(chain) in self.markov_dict:
	        next_word = choice(self.markov_dict[str(chain)])
	        text.append(next_word)
	        chain = (chain[1], next_word)

	    return " ".join(text)
