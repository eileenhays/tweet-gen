Markov Tweet Generator, 2017

Setup/Installation

### Requirements ###
	Python 2.7
	Twitter API access: 
		* Consumer Key
		* Consumer Secret
		* Access Token Key
		* Access Token Secret

#### Steps to run app locally ###

1. Clone tweet-generator repository from Github 

2. Create a virtual environment in markov_twitter directory:
$ virtualenv env

3. Activate the virtual environment:
$ source env/bin/activate

4. Install dependencies:
$ pip install -r requirements.txt

5. Create a Twitter App to get authoriation to make
secure requests to API endpoint. 
https://apps.twitter.com/app

6. Save Twitter API access info in secrets.sh file.

7. Store secets.sh as environmental variables for security. 
$ source secrets.sh

8. Run app from the command line:
$ python server.py


### View in browser ###

1. View web app in the browser
localhost:5000 

2. Enter Twitter screen name in form, submit, and view 
generated tweets!  

