'''
In this program, we will generate a three word clouds from tweet data.
One for positive tweets, one for negative, and one for neutral tweets.

For students who finish this part of the program quickly,
they might try it on the larger JSON file to see how much longer that takes.
They might also want to try subjective vs objective tweets.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Wrap this in a function because we'll use it several times
def get_filtered_dictionary(tweetblob, tweet_search):
	#Filter Words
	words_to_filter = ["about", "https", "in", "the", "thing", "will", "could", tweet_search]
	filtered_dictionary = dict()

	for word in tweetblob.words:
		#skip tiny words
		if len(word) < 2:
			continue
		#skip words with random characters or numbers
		if not word.isalpha():
			continue
		#skip words in our filter
		if word.lower() in words_to_filter:
			continue
		#don't want lower case words smaller than 5 letters
		if len(word) < 5 and word.upper() != word:
			continue;

		#Try lower case only, try with upper case!
		filtered_dictionary[word.lower()] = tweetblob.word_counts[word.lower()]

	return filtered_dictionary

#Wrap this in a function so we can use it three times
def add_figure(filtered_dictionary, plotnum, title):
	wordcloud = WordCloud().generate_from_frequencies(filtered_dictionary)
	plt.subplot(plotnum)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.title(title)
	plt.axis("off")

#Search term used for this tweet
#We want to filter this out!
tweet_search = "automation"

#Get the JSON data
tweet_file = open("tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#Combine All the Tweet Texts
positive_tweets = ""
negative_tweets = ""
neutral_tweets = ""
for tweet in tweet_data:
	tweetblob = TextBlob(tweet['text'])
	#Play with the numbers here
	if tweetblob.polarity > 0.2:
		positive_tweets += tweet['text']
	elif tweetblob.polarity < -0.2:
		negative_tweets += tweet['text']
	else:
		neutral_tweets += tweet['text']

#Create a Combined Tweet Blob
positive_blob = TextBlob(positive_tweets)
negative_blob = TextBlob(negative_tweets)
neutral_blob = TextBlob(neutral_tweets)

#Create a matplotlib figure
plt.figure(1)

#Create the three word clouds
add_figure(get_filtered_dictionary(negative_blob, tweet_search), 131, "Negative Tweets")
add_figure(get_filtered_dictionary(neutral_blob, tweet_search), 132, "Neutral Tweets")
add_figure(get_filtered_dictionary(positive_blob, tweet_search), 133, "Positive Tweets")

#Show all at once
plt.show()
