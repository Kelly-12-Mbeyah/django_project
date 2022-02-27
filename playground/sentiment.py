import http.client
import json

from flair.models import TextClassifier
from flair.data import Sentence
from textblob import TextBlob

conn = http.client.HTTPSConnection("api.twitter.com")
key = api_key = 'waVpaLs0R2sPLtYnYmgfE2ZQr'
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF2yYwEAAAAA3yJNIbNKWWV24mbB%2FhpE%2BQXWuuM%3DLXdMfVIeGSGbKPxcfSi2o0sEPpjFK6NZ2flgfXwbOi22ylgYxw'
}
payload = {}
params = '/2/tweets/search/recent?query=ukraine'

{
    "data": [{},{},{},{}]
}

conn.request("GET", params, payload, headers=headers)

response = conn.getresponse()

try:
    data = json.load(response)
    tweets = data['data']
    # {
    #     "data": [{},{},{},{}]
    # }
    for tweet in tweets:
        print(tweet['text'])
    def get_tweet_sentiment(self, tweet):
            '''
            Utility function to classify sentiment of passed tweet
            using textblob's sentiment method
            '''
		# create TextBlob object of passed tweet text
	    analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, query, count = 10):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []
        # Classify tweet['text'] using Ref: https://realpython.com/python-nltk-sentiment-analysis/
except ValueError:
    print(ValueError)





