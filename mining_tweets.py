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
