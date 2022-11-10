import feedparser

NewsFeed = feedparser.parse("https://tvn24.pl/najnowsze.xml")

n = len(NewsFeed.entries)

for i in range(n):
  entry = NewsFeed.entries[i]
  print (entry.title)