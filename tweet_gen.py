import os
import sys
from random import choice
import twitter


# class Tweets(object):
api = twitter.Api(
                  consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
                  consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
                  access_token_key=os.environ.get("TWITTER_ACCESS_TOKEN_KEY"),
                  access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
                  )

print api.VerifyCredentials()

statuses = api.GetUserTimeline(screen_name='eileenbeenleft')
print [s.text for s in statuses]

# def search_tweets(screen_name):
#     """Search tweets given a screen_name."""

#     TWITTER_API_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
#     payload = {'screen_name' = screen_name,
#                   'exclude_replies' = 'true',
#                   'include_rts' = 'false'
#     }

#     tweets = requests.get(TWITTER_API_URL, params=payload)

#     return tweets.json()


# def make_chains(tweet_data):
#     """Takes tweet text as string; returns dictionary of markov chains."""

#     # if "text" in tweet_data["tweet"]: 
#     chains = {}

#     words = text_string.split()

#     for i in range(len(words) - 2):
#         key = (words[i], words[i + 1])
#         value = words[i + 2]

#         if key not in chains:
#             chains[key] = []

#         chains[key].append(value)

#         # or we could replace the last three lines with:
#         #    chains.setdefault(key, []).append(value)

#     return chains


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""



#     key = choice(chains.keys())
#     words = [key[0], key[1]]
#     count = len(key[0] + key[1]) + 2
#     while key in chains:
#         # Keep looping until we have a key that isn't in the chains
#         # (which would mean it was the end of our original text)
#         #
#         # Note that for long texts (like a full book), this might mean
#         # it would run for a very long time.

#         word = choice(chains[key])
#         if count < 140 - len(word):
#             count = count + len(word) + 1 #include extra space after word
#             words.append(word)
#             key = (key[1], word)
#         else:
#             break

#     return " ".join(words)


# def tweet(chains):
#     # Use Python os.environ to get at environmental variables
#     # Note: you must run `source secrets.sh` before running this file
#     # to make sure these environmental variables are set.
#     user_input = None
#     tweet = make_text(chains)
#     print tweet

#     while True:
#         print ""
#         user_input = raw_input("Do you want to tweet this? [t for tweet, r for regenerate, q to quit] ")
#         if user_input == "t":
#             status = api.PostUpdate(tweet)
#             print status.text
#         elif user_input == "r":
#             print ""
#             tweet = make_text(chains)
#             print tweet
#             print ""
#         elif user_input == "q":
#             break
#             # else:


# # Get the filenames from the user through a command line prompt, ex:
# # python markov.py green-eggs.txt shakespeare.txt
# filenames = sys.argv[1:]

# # Open the files and turn them into one long string
# text = open_and_read_file(filenames)

# # Get a Markov chain
# chains = make_chains(text)
# # print chains

# # text = make_text(chains)


# # Your task is to write a new function tweet, that will take chains as input
# tweet(chains)
