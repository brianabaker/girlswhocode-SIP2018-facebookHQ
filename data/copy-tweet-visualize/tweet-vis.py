import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# import wordcloud from WordCloud

#Get the JSON data
tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

tweet_polarity = []
tweet_subjectivity = []

for tweet in tweet_data:
    text = TextBlob(tweet["text"])
    tweet_polarity.append(text.sentiment.polarity)
    tweet_subjectivity.append(text.sentiment.subjectivity)

tweet_search = "automation"

combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet["text"]

tweetblob = TextBlob(combined_tweets)

words_to_filter = ["about", "https", "thing", "will", "could", tweet_search]

filtered_dictionary = dict()

for word in tweetblob.words:
    print(word)
    if len(word) < 2:
        continue
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    if len(word) < 5 and word.upper() != word:
        continue

    filtered_dictionary[word.lower()] = tweetblob.word_counts[word.lower()]


wordcloud = WordCloud().generate_from_frequencies(filtered_dictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
