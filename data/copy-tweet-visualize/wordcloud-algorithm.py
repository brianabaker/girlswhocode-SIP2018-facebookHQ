import json
# from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

# this is the keyword so i want to filter it out
tweet_search = "automation"

# i want to use the text for all the tweets, so i need the tweets to be in one string
combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet["text"]


cleaned_tweets = re.sub(r'[^\w\s]', '', combined_tweets)

print(cleaned_tweets)

words_to_filter = ["about", "https", "thing", "will", "could", tweet_search]

filtered_words= []
# i've filtered through the cleaned tweets
for word in cleaned_tweets.split():
    if len(word) < 5:
        continue
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    filtered_words.append(word)
print(filtered_words)

# now i need to do the county thing
# so i got my list
# i need an empty dictionary
word_count = {}
# in this empty dictionary, i'm going to add the word count as a value to the word as a key
# so i need to iterate through my filtered_words list
# and add each word as a key with the value of 1,

# checking if it already exists, and incrementing it by 1 if it does
for word in filtered_words:
    if word.lower() not in word_count:
        word_count[word.lower()] = 1
    else:
        word_count[word.lower()] += 1

print(word_count)


# WORDCLOUD STUFF
wordcloud = WordCloud().generate_from_frequencies(word_count)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
