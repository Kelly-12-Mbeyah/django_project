import http.client
import json
import re


from flair.models import TextClassifier
from flair.data import Sentence
from textblob import TextBlob

# import pandas as pd
# import numpy as np
# import re
# import nltk
# from nltk.corpus import stopwords

# from keras.preprocessing.text import one_hot
# from keras.preprocessing.sequence import pad_sequences
# from keras.models import Sequential
# from keras.layers.core import Activation, Dropout, Dense
# from keras.layers import Flatten
# from keras.layers import GlobalMaxPooling1D
# from keras.layers.embeddings import Embedding
# from keras.preprocessing.text import Tokenizer

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    print("#################")
    print(tweet)
    
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    #create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    #analysis = TextBlob(tweet)

    #set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# def predict_sentiment(tweet):
#     model = Sequential()
#     instance = tokenizer.texts_to_sequences(instance)

#     flat_list = []
#     for sublist in instance:
#         for item in sublist:
#             flat_list.append(item)

#     flat_list = [flat_list]

#     instance = pad_sequences(flat_list, padding='post', maxlen=maxlen)

#     print(model.predict(instance))

conn = http.client.HTTPSConnection("api.twitter.com")
key = api_key = 'waVpaLs0R2sPLtYnYmgfE2ZQr'
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF2yYwEAAAAA3yJNIbNKWWV24mbB%2FhpE%2BQXWuuM%3DLXdMfVIeGSGbKPxcfSi2o0sEPpjFK6NZ2flgfXwbOi22ylgYxw'
}
payload = {}
params = '/2/tweets/search/recent?query=uda'


conn.request("GET", params, payload, headers=headers)

response = conn.getresponse()

try:
    data = json.load(response)
    tweets = data['data']

    for tweet in tweets:
        tweet_sentiment = get_tweet_sentiment(tweet["text"])
        #predict_sentiment(tweet["text"])
        print(tweet_sentiment)

except ValueError:
    print(ValueError)




	# def get_tweets(self, query, count = 10):
	# 	'''
	# 	Main function to fetch tweets and parse them.
	# 	'''
	# 	# empty list to store parsed tweets
	# 	tweets = []
    #     # Classify tweet['text'] using Ref: https://realpython.com/python-nltk-sentiment-analysis/





