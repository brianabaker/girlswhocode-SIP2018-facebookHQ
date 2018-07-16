'''
In this program, we store the polarities and subjectivities of all the tweets.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweet_file = open("tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#Create a Sentiment List
polarity_list = []

#[OPTIONAL] Subjectivity
subjectivity_list = []

#Get Sentiment Data
for tweet in tweet_data:
	tweetblob = TextBlob(tweet["text"])
	polarity_list.append(tweetblob.polarity)

	#[OPTIONAL] Subjectivity
	subjectivity_list.append(tweetblob.subjectivity)

print(polarity_list)
print(subjectivity_list)
