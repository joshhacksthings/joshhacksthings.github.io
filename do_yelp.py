import io, json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from flask import Flask, render_template

app = Flask(__name__)

# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

def getRestaurant(words):
	location = "Phoenix"
	return client.search(term=words, location=location)

def show_me_more(words):
	for x in getRestaurant(words).businesses:
		print(x.id)



# doing Flask things
# FIX THISSSSS
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/rest-picker/')
def GR():
	return show_me_more('thai')

if __name__ == '__main__':
  app.run(debug=True)

