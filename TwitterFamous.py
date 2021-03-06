"""
Copyright 2015

@author Yoko Yamaguchi, Nicholas Vega, Connor McCarl, Adrienne Bergh

Twitter Famous

"""
from __future__ import print_function
from twitter import Twitter, OAuth, TwitterHTTPError
import sys
import random
from datetime import datetime

created_at_format = '%a %b %d %H:%M:%S +0000 %Y'


class TwitterFamous:
	def __init__(self):
		self.config = {}
		self.connection = None
		random.seed()

	def setup(self):
		with open("config.txt", "r") as infile:
			for line in infile:
				line = line.split(":")
				parameter = line[0].strip()
				value = line[1].strip()
				self.config[parameter] = value

		self.connection = Twitter(auth=OAuth(self.config["OAUTH_TOKEN"],
											 self.config["OAUTH_SECRET"],
											 self.config["CONSUMER_KEY"],
											 self.config["CONSUMER_SECRET"]))
		print("Your Authenticated.")
		print(self.connection)

	def search_tweets(self, word, count, result_type="recent"):
		return self.connection.search.tweets(q=word, result_type=result_type, count=count)

	def favorite_tweets(self, word, count, result_type="recent"):
		result = self.search_tweets(word, count, result_type)
		for tweet in result["statuses"]:
			try:
				result = self.connection.favorites.create(_id=tweet["id"])
				print("Favorited: %s" % (result["text"].encode("utf-8")), file=sys.stdout)
			except TwitterHTTPError as api_error:
				print("ERROR")

	def retweet(self, word, count, result_type="recent"):
		result = self.search_tweets(word, count, result_type)
		for tweet in result["statuses"]:
			try:
				result = self.connection.statuses.retweet(id=tweet["id"])
				print("Retweeted: %s" % (result["text"].encode("utf-8")), file=sys.stdout)
			except TwitterHTTPError as api_error:
				print("ERROR")

	def follow(self, word, count, result_type="recent"):
		result = self.search_tweets(word, count, result_type)
		for tweet in result["statuses"]:
			try:
				self.connection.friendships.create(user_id=tweet["user"]["id"], follow=False)
				print("Followed %s" %
							(tweet["user"]["screen_name"]), file=sys.stdout)
			except TwitterHTTPError as api_error:
				print("ERROR")

	def geo_search(self, latitude, longitude):
		max_range = 1 			# search range in kilometres
		try:
			query = self.connection.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 10)
			for result in query["statuses"]:
				if result["geo"]:
					try:
						self.connection.friendships.create(user_id=result["user"]["id"], follow=False)
						print("Followed %s" %
									(result["user"]["screen_name"]), file=sys.stdout)
					except TwitterHTTPError as api_error:
						print("ERROR")
		except Exception:
			print ("ERROR")

	def tweet_rate(self):
		terms = raw_input("Please enter a term:")
		query = self.connection.search.tweets(q = terms)
		results = query["statuses"]
		first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
		last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
		total_dt = (first_timestamp - last_timestamp).total_seconds()
		mean_dt = total_dt / len(results)
		print("Average tweeting rate for '%s' between %s and %s: %.3fs" % (terms, results[-1]["created_at"], results[0]["created_at"], mean_dt))

	def post_status(self, new_status):
		try: 
			result = self.connection.statuses.update(status = new_status)
			print( "New status: %s" % new_status)
		except TwitterHTTPError as api_error:
			print("ERROR")

	def print_newsfeed(self):
		try:
			statuses = self.connection.statuses.home_timeline(count = 50)
			for status in statuses:
				print( "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))
		except TwitterHTTPError as api_error:
			print("ERROR")
