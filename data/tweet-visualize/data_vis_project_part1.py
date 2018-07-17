'''
In this program, we store the polarities and subjectivities of all the tweets.
'''

import json
from textblob import TextBlob

#Get the JSON data
tweet_file = open("tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#Create a Sentiment List
polarity_list = []

#Create a Subjectivity List
subjectivity_list = []

#Get Sentiment Data
for tweet in tweet_data:
    tweetblob = TextBlob(tweet["text"])
    polarity_list.append(tweetblob.polarity)
    subjectivity_list.append(tweetblob.subjectivity)


# maybe do the counter thing to show them there are 99 tweets in here
# print(polarity_list)
# print(subjectivity_list)


# MAYBE SHOW THIS MAYBE DON'T SHOW THEM THIS
#This can be useful to see what's possible
#to do with a Textlob object
# print('DIR', dir(tweetblob))
print(TextBlob("very great").sentiment)
print(TextBlob("i love you").subjectivity)
