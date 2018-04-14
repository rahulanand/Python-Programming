'''
    Author: Rahul
    Title: Find Who tweeted most

'''

from collections import OrderedDict

#number of test cases
t = int(input())

#input tweets as list
tweets = []

for i in range(0,t):
    z = int(input())
    for j in range(0, z):
        y = input()
        tweets.append(y)

# dictionary for counting the no, of tweets
count_tweets = {}

#adding name and no. of tweets in to dictionary
for tweet in tweets:
    var = tweet.split(" ")
    if var[0] in count_tweets.keys():
        count_tweets[var[0]] = count_tweets[var[0]] + 1
    else:
        count_tweets[var[0]] = 1

#sorting according to name
sorted_tweets_count = OrderedDict(sorted(count_tweets.items()))

for key, value in sorted_tweets_count.items():
    if sorted_tweets_count[key] > 1:

        print("{} {}".format(key, value))
