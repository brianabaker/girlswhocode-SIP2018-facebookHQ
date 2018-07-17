'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweet_file = open("TwitterData/tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

# Continue your program below!

# Textblob sample:
tweet_blob = TextBlob("You are a brilliant computer scientist.")
print(tweet_blob.polarity)
