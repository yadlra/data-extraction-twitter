import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Cursor
import json
import pandas as pd
import csv
import unicodecsv
from unidecode import unidecode
import datetime
import pandas


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users = []


with open('tweets.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter=',', quotechar='"')

    writer.writerow(["user_name",
                     "user_username",
                     "user_followers_count",
                     "user_listed_count",
                     "user_following",
                     "user_favorites",
                     "user_verified",
                     "user_default_profile",
                     "user_location",
                     "user_time_zone",
                     "user_statuses_count",
                     "user_description",
                     "user_geo_enabled",
                     "user_contributors_enabled",
                     "tweet_year",
                     "tweet_month",
                     "tweet_day",
                     "tweet_hour",
                     "tweet_text",
                     "tweet_lat",
                     "tweet_long",
                     "tweet_source",
                     "tweet_in_reply_to_screen_name",
                     "tweet_direct_reply",
                     "tweet_retweet_status",
                     "tweet_retweet_count",
                     "tweet_favorite_count",
                     "tweet_hashtags",
                     "tweet_hashtags_count",
                     "tweet_urls",
                     "tweet_urls_count",
                     "tweet_user_mentions",
                     "tweet_user_mentions_count",
                     "tweet_media_type",
                     "tweet_contributors"])

  for user in users:
    user_obj = api.get_user(user)

    user_info = [user_obj.name,
                 user_obj.screen_name,
                 user_obj.followers_count,
                 user_obj.listed_count,
                 user_obj.friends_count,
                 user_obj.favourites_count,
                 user_obj.verified,
                 user_obj.default_profile,
                 user_obj.location,
                 user_obj.time_zone,
                 user_obj.statuses_count,
                 user_obj.description,
                 user_obj.geo_enabled,
                 user_obj.contributors_enabled
                 ]

  for tweet in Cursor(api.user_timeline, screen_name = user).items(20):
      direct_reply = True if tweet.in_reply_to_screen_name != "" else False
      retweet_status = True if tweet.text[0:3] == "RT" else False

      tweet_info = [tweet.created_at.year,
                    tweet.created_at.month,
                    tweet.created_at.day,
                    tweet.created_at.hour,
                    unidecode(tweet.text),
                    lat,
                    long,
                    tweet.source,
                    tweet.in_reply_to_screen_name,
                    direct_reply,
                    retweet_status,
                    tweet.retweet_count,
                    tweet.favorite_count
                    ]

hashtags = []
      hashtags_data = tweet.entities.get('hashtags', None)
      if(hashtags_data != None):
        for i in range(len(hashtags_data)):
          hashtags.append(unidecode(hashtags_data[i]['text']))

urls = []
      urls_data = tweet.entities.get('urls', None)
      if(urls_data != None):
        for i in range(len(urls_data)):
          urls.append(unidecode(urls_data[i]['url']))

  user_mentions = []
      user_mentions_data = tweet.entities.get('media', None)
      if(user_mentions != None):
        for i in range(len(user_mentions)):
          user_mentions.append(unidecode(user_mentions_data[i]['screen_name']))

media = []
      media_data = tweet.entities.get('media', None)
      if(media_data != None):
        for i in range(len(media_data)):
          media_data.append(unidecode(media_data[i]['type']))
