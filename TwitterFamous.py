"""
Copyright 2015

@author Yoko Yamaguchi, Nicholas Vega, Conner McCarl, Adrienne Bergh

Twitter Famous

"""
from __future__ import print_function
from twitter import Twitter, OAuth, TwitterHTTPError
import sys
import random

class TwitterFamous:

    def __init__(self):
        self.config = {}
        self.connection = None
        random.seed()

    def setup(self):
        self.connection = Twitter(auth=OAuth("2257085569-AcqPChcHvIXDpSCnZFsoPx9QFKarj08wxDPR3Nl",
                                                     "hPvAgF7Lo2KWjBLZzdFZI7uF1H8WDORUdXHzOwQzbQUiL",
                                                     "TGMsKkUheVYhcjF4A3P0Ljlca",
                                                     "YsM8FCFaRXI4heh4dMj3eJU7WGWuYwlmWIgQGByWocnOiZlK5y"))
        print("Your Authenticated.")
        print(self.connection)

    def search_tweets(self, word, count=10, result_type="recent"):
        return self.connection.search.tweets(q=word, result_type=result_type, count=count)

    def favorite_tweets(self, word, count=10, result_type="recent" ):
        result = self.search_tweets(word, count, result_type)
        for tweet in result["statuses"]:
            try:
                result = self.connection.favorites.create(_id=tweet["id"])
                print("Favorited: %s" % (result["text"].encode("utf-8")), file=sys.stdout)
            except TwitterHTTPError as api_error:
                print("ERROR")

