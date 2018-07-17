import json

# how do we open a tweet file into our python?

# are we going to write anything to it?
file = open("tweets_small.json", "r")
tweet_data = json.load(file)
file.close()

print(tweet_data)
# so now i have all that json data, in the variable called tweet_data

# this is like, a lot of data right?

# Let's try to take a look at it a bit

# how do you think I look at just the first one in this list?
# ########

# DO it without the first tweet first and then with the first tweet: thing after
# print("First tweet: ", tweet_data[0])
# let's print the id?
# take a look at the Tweet object
# print("Tweet id: ", tweet_data[0]["id"])
# print('')
# print("Text: ", tweet_data[0]["text"])
# print('')
# print("User: ", tweet_data[0]["user"])
# print('')
# print("Hashtags: ", tweet_data[0]["hashtags"])
# print('')
# print("URLS: ", tweet_data[0]["urls"])
# print('')
# print("user_mentions: ", tweet_data[0]["user_mentions"])
# THIS WASN'T GEOTAGGED -- SO THERE IS NO PLACE

# Great! so....
# how might we use loops to just print ONLY the text of each tweet? ???
# I'm going to give you a couple minutes to try to figure it out in pairs, talk it out.

# ONE WAY TO DO IT WITH RANGE
# for index in range(len(tweet_data)):
#     print("Tweet text: " + tweet_data[index]["text"])
#     print('')

# but! since we are also just grabbing it at that element, and we're not grabbing from two dictionaries, or two lists, we can use the other

# ANOTHER WAY TO DO IT NOT WITH RANGE
for tweet in tweet_data:
    print(tweet["hashtags"])
    print('')

# for tweet in tweet_data:
#     print('hashtags: ' + tweet["hashtags"])
#     print('')
    # YASSSSSS
