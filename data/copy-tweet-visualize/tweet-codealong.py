
# into looking at this data

# we have json file
# we have to load it into this python file

import json

file = open("tweets-small.json", "r")

tweet_data = json.load(file)

file.close()

# print out only text from ALL the TWEETS
# OPTION ONE
for idx in range(len(tweet_data)):
    print("Tweet text: ", tweet_data[idx]["text"])
    print('')
# OPTION TWO
for tweet in tweet_data:
    print(tweet["text"])
    print('')
