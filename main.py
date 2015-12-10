"""
Copyright 2015

@author Yoko Yamaguchi, Nicholas Vega, Connor McCarl, Adrienne Bergh

Twitter Famous

"""
from TwitterFamous import TwitterFamous
from pyfiglet import figlet_format
from geopy.geocoders import Nominatim

tf = TwitterFamous()
tf.setup()

print(figlet_format('Wanna be TwitterFamous?', font='big'))
print("Menu...")
print("1. Favorite Random Tweets")
print("2. Retweet Random Tweets")
print("3. Follow Random People")
print("4. Follow people near you")
print("5. Determine the tweet rate for any term/phrase")
print("6. Print last 50 items on Twitter newsfeed")
print("7. Post a tweet")
print("8. Print out all Followers")
menu = input("Choose: ")
if menu == 1:
    keyword = raw_input("Pick a keyword:")
    count = raw_input("Count:")
    tf.favorite_tweets(keyword, count)
if menu == 2:
    keyword = raw_input("Pick a keyword:")
    count = raw_input("Count:")
    tf.retweet(keyword, count)
if menu == 3:
    keyword = raw_input("Pick a keyword:")
    count = raw_input("Count:")
    tf.follow(keyword, count)
if menu == 4:
		geolocator = Nominatim()
		address = raw_input("Enter your current location i.e. 175 5th Avenue NYC: ")
		location = geolocator.geocode(address)
		print("Your current location is :" + str(location.latitude) + str(location.longitude))
		tf.geo_search(location.latitude, location.longitude)
if menu == 5:
    tf.tweet_rate()
if menu == 6:
	tf.print_newsfeed()
if menu == 7:
	new_status = raw_input("Enter a status to post: ")
	tf.post_status(new_status)
if menu == 8:
	keyword = raw_input("Pick a username:")
	tf.print_followers(keyword)
