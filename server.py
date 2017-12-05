from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, session)
from flask_debugtoolbar import DebugToolbarExtension
import os
import twitter
from tweet_gen import UserTweets
# from sys import argv
# from random import choice

### FLASK ###
app = Flask(__name__)
app.secret_key = "ABC"


# Raises an error in Jinja
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""

    print str(session)
    return render_template("index.html", screen_name=None, tweet=None)


@app.route('/initial-tweet')
def save_session_and_first_tweet():
    """Initial generated tweet with a new screen name"""

    screen_name = request.args.get('screen-name')
    if '@' in screen_name:
        screen_name = screen_name.replace('@', '')

    try:
        clean_sn = UserTweets(screen_name)
        tweet_text = clean_sn.random_tweet_generator()
        session['curr_sn'] = screen_name
        
        if not session['gen_tweets']:
            session['gen_tweets'] = [tweet_text]
        else:
            all_tweets = session['gen_tweets']
            all_tweets.append(tweet_text)
            session['gen_tweets'] = all_tweets
    except:
        print "Entry error. Try again."
        clean_sn = None
        tweet_text = "Entry error. Try again."

    return render_template("index.html", screen_name=clean_sn, tweet=tweet_text)


@app.route('/new-tweet')
def generate_new_tweet():
    """Returns a new randomly generated tweet using current screen name"""

    new_tweet = None 

    current_sn = session['curr_sn']
    print current_sn
    sn_instance = UserTweets(current_sn)
    new_tweet = sn_instance.random_tweet_generator()
    gen_tweets = session['gen_tweets']
    gen_tweets.append(new_tweet)
    session['gen_tweets'] = gen_tweets
    print str(session)

    return new_tweet  


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True
    # app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
