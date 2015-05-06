from twython import TwythonStreamer

tweets = []

class MyStreamer(TwythonStreamer):
	
	def on_success(self,data):
		if data['lang'] == 'en':
			tweets.append(data)
			print "received tweet #",len(tweets)

		if len(tweets) >= 1000:
			self.disconnect()

	def on_error(self,status_code,data):
		print status_code, data
		self.disconnect()



try:
	CONSUMER_KEY = sys.argv[1]
	CONSUMER_SECRET = sys.argv[2]
	ACCESS_TOKEN    = sys.argv[3]
	ACCESS_TOKEN_SECRET = sys.argv[4]
except:
	print "usage: twitter_streamer.py CONSUMER_KEY CONSUMER_SECRET ACCESS_TOKEN ACCESS_TOKEN_SECRET"
	sys.exit(1)

stream = MyStreamer(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,								ACCESS_TOKEN_SECRET)

stream.statuses.filet(track='data')
#stream.status.sample()

top_hashtags = Counter(hashtag['text'].lower()
					   for tweet in tweets
					   for hashtag in tweet["entities"]["hashtags"])

print top_hashtags.most_common(5)

#probably want to use pandas for exporting data
#maybe use scrapy for web scrapers