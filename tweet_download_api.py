import tweepy # Twitter api
import csv
import time

# based on code used from gist.github.com/yanofsky/5436496
# additions: taking more fields of data (necessary try/except for blank fields like 'sensitive'), try/except condition, parameter changes, inserted unique delimiter ',\t,'

# Credentials
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
# Name of user of interest
screen_name = ''


# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# initialize list for all tweepy tweets
alltweets= list()

# initial request for most recent tweets (200 is max allowed count) 3200 max after max requests
new_tweets = api.user_timeline(screen_name = screen_name, count = 200, exlude_replies= 'true')

# save most recent tweets
alltweets.extend(new_tweets)

# save the id of the oldest tweet less one
oldest = alltweets[-1].id -1

# keep grabbing tweets until there are no tweets left to grab
while len(new_tweets)> 0:
    print 'getting tweets before %s' % (oldest)

    # all subsequent requests use the max_id parameter to prevent duplicates
    try:
        new_tweets = api.user_timeline(screen_name= screen_name, count = 200, max_id = oldest, exlude_replies= 'true')

        # save most recent tweets
        alltweets.extend(new_tweets)

        # save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        time.sleep(120)

        print '...%s tweets downloaded so far' % (len(alltweets))
    except:
        print 'DOWNLOAD SAFEGUARD TRIGGERED', ' ', '...%s tweets downloaded so far' % (len(alltweets))
        break

# inserting unique delimiter and saving
outtweets = list()
for tweet in alltweets:
    try: sensitive = tweet.possibly_sensitive
    except: sensitive = False
    buildingobs = [tweet.id_str, '\t', tweet.created_at, '\t', tweet.text.encode('utf-8'), '\t', tweet.favorite_count, '\t', tweet.retweet_count, '\t', tweet.source, '\t', tweet.truncated, '\t', tweet.retweeted, '\t', tweet.is_quote_status, '\t', sensitive, '\t', tweet.lang, '\t', tweet.entities, '\t', tweet.coordinates, '\t', tweet.place, '\t', tweet.user]
    outtweets.append(buildingobs)

labels= ['id', '\t', 'created_at', '\t', 'text', '\t', 'favorites', '\t', 'retweets', '\t', 'source', '\t', 'truncated', '\t', 'is_retweet', '\t', 'is_quote_status', '\t', 'possibly_sensitive', '\t', 'lang', '\t', 'entities', '\t', 'coordinates', '\t', 'place', '\t', 'user']

with open('%s_tweets.csv' % screen_name, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(labels)
    writer.writerows(outtweets)
