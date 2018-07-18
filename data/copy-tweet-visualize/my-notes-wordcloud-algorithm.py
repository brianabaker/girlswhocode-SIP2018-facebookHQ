import json
# from textblob import TextBlob
from wordcloud import WordCloud
import re


tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

# This is the search keyword, so we want to filter it about
# B/C it will be the number one
tweet_search = "automation"

# We want to grab the most common words that appear in ALL the tweets
# So we need to combine all the tweet texts as a string
# So when we're searching though it, we're looking through the whole thing.
combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet["text"]

# when we iterate on a sentence we go letter by letter, including punctuation, whitespace
# there's a cool thing called regex, which stands for regular expression. in computer programming it's most used to strip puncuation, characters, whitespace, etc. you can also add punctuation. although the .method name you use is different, the regex you use is the same for every programming language
cleaned_tweets = re.sub(r'[^\w\s]', '', combined_tweets)

filtered_words = []
# when we iterate over a string it's letter by letter
# we don't want to iterate letter by letter, we want to go by the whole word
# there's a method for that. it's called .split()
# let's print it out and see how it all works
for word in cleaned_tweets.split():
    print(cleaned_tweets)
    print(cleaned_tweets.split())
    if len(word) < 5:
        continue
    # how do we check if it's not something?
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    # we want these words to appear separate again, like in the cleaned_tweets.split()
    # so we're going to append these to a list
    filtered_words.append(word)

# this is the standard way to count words!
# we make it a dictionary
# the word is the key, and the value is the amount
word_count = {}
for word in filtered_words:
    if word.lower() not in word_count:
        word_count[word.lower()] = 1
    else:
        word_count[word.lower()] += 1


# WORDCLOUD STUFF
# wordcloud = WordCloud().generate_from_frequencies(word_count)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
