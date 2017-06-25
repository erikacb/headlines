import feedparser
from flask import Flask
from flask import render_template

app = Flask (__name__)

RSS_FEEDS = { 
	'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
	'cnn': 'http://rss.cnn.com/rss/edition.rss',
	'fox': 'http://feeds.foxnews.com/foxnews/latest',
}

RSS_TITLES = { 
	'bbc': 'BBC UK',
	'cnn': 'CNN USA',
	'fox': 'Fox News',
}

@app.route ("/")

def home():
	return "Home"

@app.route ("/<publication>")

def get_news(publication):
	feed = feedparser.parse(RSS_FEEDS[publication])
	return render_template("home.html",
		articles = feed['entries'], headline_title = RSS_TITLES[publication])

if __name__ == '__main__':
	app.run(port = 5000, debug = True)