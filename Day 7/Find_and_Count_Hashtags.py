import re
from collections import Counter, OrderedDict

no_tweets = int(input())
tweets = ''

for tweet in range(no_tweets):
    tweets += str(input())
    tweets += ' '
test_list = list(tweets.split(' '))

trend_hash = []
for tweet in test_list:
    hashtag = re.search(r'\#\w+', tweet)
    if hashtag:
        trend_hash.append(tweet)
        
class OrderedCounter(Counter, OrderedDict):
    pass
[print(most_trend[0]) for most_trend in OrderedCounter(sorted(trend_hash)).most_common(5)]
            