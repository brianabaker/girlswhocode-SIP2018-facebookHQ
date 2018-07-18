import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re


tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()
# START PART 1
tweet_polarity = []
tweet_subjectivity = []

for tweet in tweet_data:
    text = TextBlob(tweet["text"])
    tweet_polarity.append(text.sentiment.polarity)
    tweet_subjectivity.append(text.sentiment.subjectivity)

# END PART 1
tweet_search = "automation"

combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet["text"]

tweetblob = TextBlob(combined_tweets)
# this tweet blob is grabbing the hashes

words_to_filter = ["about", "https", "thing", "will", "could", tweet_search]

filtered_dictionary = {}

# when we iterate on a sentence we go letter by letter, including punctuation, whitespace
# there's a cool thing called regex, which stands for regular expression. in computer programming it's most used to strip puncuation, characters, whitespace, etc. you can also add punctuation. although the .method name you use is different, the regex you use is the same for every programming language

cleaned_tweets = re.sub(r'[^\w\s]', '', combined_tweets)

filtered_words = []
for word in cleaned_tweets.split():
    if len(word) < 5:
        continue
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    filtered_words.append(word)

# print('FILTERED WORDS')
# print(filtered_words)

word_count = {}
for word in filtered_words:
    if word.lower() not in word_count:
        word_count[word.lower()] = 1
    else:
        word_count[word.lower()] += 1


wordcloud = WordCloud().generate_from_frequencies(word_count)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
