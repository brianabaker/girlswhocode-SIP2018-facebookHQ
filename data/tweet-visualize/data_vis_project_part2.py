'''
In this program, we display a histogram of the polarities of all the tweets.

ONLY SECOND PART IS OPTIONAL
In this program, we will also display a scatter plot of polarity vs subjectivity.

For students who finish this part of the program quickly,
they might try out the optional graph. They might also try
using the larger tweet file to generate the graph (this might take a while).

They might also try to combine both graphs into one display.
They can also play around with different bins for the histogram
or try to draw centeredaxes on the scatter plot using matplotlib "spines".
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweet_file = open("tweets_small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

#Create a Sentiment List
polarity_list = []

#[OPTIONAL] Subjectivity
subjectivity_list = []

#Get Sentiment Data
for tweet in tweet_data:
	tweetblob = TextBlob(tweet["text"])
	polarity_list.append(tweetblob.polarity)
	#[OPTIONAL] Subjectivity
	subjectivity_list.append(tweetblob.subjectivity)


#Create the Graph
# the bins here are the numbers on the y axis x axis (polarity)
# between -1 and +1
plt.hist(polarity_list, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
# bins is the amount of distance they want between the x axis
# histograms are one set of data and graphs do go up and down like that
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
# this is the number of tweets
plt.axis([-1.1, 1.1, 0, 100])
# x min , x max, y min, y max
plt.grid(True)
plt.show()


#[OPTIONAL] Subjectivity
plt.plot(polarity_list, subjectivity_list, 'ro')
plt.xlabel('Polarity')
# so here it's polarity list plotting the x axis
plt.ylabel('Subjectivity')
# and here is the subjectivity list plotting the y axis
plt.title('Tweet Polarity vs Subjectivity')
# plt.axis is the x axis
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()
