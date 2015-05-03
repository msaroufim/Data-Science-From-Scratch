from twython import Twython
import sys

try:
	CONSUMER_KEY    = sys.argv[1]
	CONSUMER_SECRET = sys.argv[2]

except:
	print "usage: twitter.py CONSUMER_KEY CONSUMER_SECRET"
	sys.exit(1)

CONSUMER_KEY
CONSUMER_SECRET

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)

for status in twitter.search(q='"data science"')["statuses"]:
	user = status["user"]["screen_name"].encode('utf-8')
	text = status["text"].encode('utf-8')
	print user, ":", text
	print

#encode('utf-8') is needed since there are unicode characters that show up in up in tweets
