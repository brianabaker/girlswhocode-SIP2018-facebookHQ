'''
In this program, we will generate a word cloud from tweet data.

For students who finish this part of the program quickly,
they might try it on the larger JSON file to see what clouds they can get.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Search term used for this tweet
#We want to filter this out!
# so... heads up! if you hadn't noticed the search term for this data is automation
tweet_search = "automation"

#Get the JSON data
tweet_file = open("tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#Combine All the Tweet Texts
# you have to combine all the tweets in one large string!
# it doesn't care who wrote what
combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet['text']

#Create a Combined Tweet Blob
tweetblob = TextBlob(combined_tweets)

#This can be useful to see what's possible
#to do with a Textlob object
# print('DIR', dir(tweetblob))

#Filter Words
words_to_filter = ["about", "https", "in", "the", "thing", "will", "could", tweet_search]
# words_to_filter = ["to", "with", "at", "and", "is", "by", "for", "it", "if", "of", "when", "about", "https", "in", "the", "thing", "will", "could", tweet_search]
filtered_dictionary = dict()

# HOW DO WE SKIP over thing IN PYTHON?
# tweetblob.words literally just grabs the words from the blob.
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
        #this is just making sure it's not an accronym
        continue

	#Try lower case only, try with upper case!
    filtered_dictionary[word.lower()] = tweetblob.word_counts[word.lower()]
    # has to be lower! because there's not so many upper case words
    # this makes a word count dictionary
    # because the tweetblob has a word_counts method which returns how many times the word is in the blob


#Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filtered_dictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
