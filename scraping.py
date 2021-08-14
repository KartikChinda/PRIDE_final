# Consumer Key "has now been removed"
# Consumer Secret "has now been removed"
# Access Token "has now been removed"
# Access Token "has now been removed"


import json
import csv
import tweepy
import re


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):

    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initialize Tweepy API
    api = tweepy.API(auth)

    # create a spreadsheet
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    # open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'w', encoding="utf-8") as file:

        w = csv.writer(file)

        # write the headings to the spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username',
                   'all_hashtags', 'followers_count'])

        # for each tweet matching our hashtags, write the tweet into the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(100):
            # print(tweet.full_text)
            w.writerow([tweet.created_at, tweet.full_text.replace('\n', ' ').encode('utf-8'), tweet.user.screen_name.encode(
                'utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])


consumer_key = input('Consumer Key ')
consumer_secret = input('Consumer Secret ')
access_token = input('Access Token ')
access_token_secret = input('Access Token Secret ')

hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret,
                        access_token, access_token_secret, hashtag_phrase)
