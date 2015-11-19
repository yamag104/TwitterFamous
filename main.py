from TwitterFamous import TwitterFamous
from pyfiglet import figlet_format

tf = TwitterFamous()
tf.setup()

print(figlet_format('Wanna be TwitterFamous?', font='big'))
print("Menu...")
print("1. Favorite Random Tweets")
print("2. Retweet Random Tweets")
print("3. Follow Random People")
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