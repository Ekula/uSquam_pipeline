from datetime import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
from flask_restful import Resource
from flask import request, jsonify
from filter_elastic import filter_elastic


# Get request to:
# host:port/requesters/crawlTweets?hashtag=tudelft&number=3
# will return a json with the last 3 tweets that contain #tudelft.
class TwitterCrawler(Resource):
    def get(self):
        hashtag = '#' + request.args.get('hashtag')
        ignored_hashtag = str(request.args.get('ignored_hashtag'))
        number = request.args.get('number')

        if hashtag is not None and number is not None and number.isdigit():
            hashtag = str(hashtag)
            number = int(number)
        else:
            # Error
            return 'Wrong input parameters, try ?hashtag=tudelft&number=50', 404

        # Successful request
        print 'GET request:  Requested ' + str(number) + ' tweets with hashtag: ' + str(hashtag) + '.'

        crawled_tweets_list = []

        consumer_key = '0tqrIxEVCdJiziTsng9QcOoEJ'
        consumer_secret = 'H4JgzHBDhLtKxuYg9tDuXySVxMioYYoqZCXL1cCn2POAPkVfdh'
        access_token = '774227310367109120-VvqXuw2b5bjqar6EiML5lJL7xprwNsi'
        access_token_secret = 'Ms295kCa0YV0NeFOwU0BpF23ElEkX0Wv7p8lQQH2jUm5v'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # search_results = api.search(q=hashtag, count=number)
        if number == 0:
            search_results = []
        else:
            search_results = [status for status in tweepy.Cursor(api.search, q=hashtag).items(number)]

        for tweet in search_results:
            tweet_json = tweet._json

            # Get hashtags list
            hashtags_list = []
            for item in tweet_json['entities']['hashtags']:
                hashtags_list.append(item['text'])

            # Get tweet's text
            if 'retweeted_status' in tweet_json:
                tweet_text = tweet_json['retweeted_status']['text']
            else:
                tweet_text = tweet_json['text']

            # Reformat json to contain less properties
            crawled_tweet = {'user_name': tweet_json['user']['screen_name'],
                             'tweet_text': tweet_text,
                             'hashtags_list': hashtags_list,
                             'created_at': tweet_json['created_at']}
            crawled_tweets_list.append(crawled_tweet)


            # print 'user_name: ' + tweet_json['user']['screen_name']
            # print 'tweet_text: ' + tweet_json['text']
            # print 'hashtags_list: ' + str(hashtags)
            # print 'created_at: ' + str(tweet_json['created_at'])
            # # print 'timestamp: ' + str(datetime.fromtimestamp(int(float(data['timestamp_ms']) / 1000.0)))
            # print '--------------------------------'

        # If list is not empty
        if crawled_tweets_list:
            crawled_tweets_list = filter_elastic(crawled_tweets_list, ignored_hashtag)
            return jsonify(results=crawled_tweets_list)
        else:
            return None, 404
