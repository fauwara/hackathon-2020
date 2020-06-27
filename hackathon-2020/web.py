import urllib, os, requests, datetime, subprocess
import feedparser

data = []

def Indian_News():
    newsfeed = feedparser.parse(
        "http://feeds.feedburner.com/ndtvnews-india-news"
    )

    for i in range(0, 10):
        entry = newsfeed.entries[i]
        
        # print(entry.title)
        # print(entry.summary)
        # print(entry.link)

        data.append({
            "title" : entry.title,
            "summary" : entry.summary,
            "link" : entry.link 
            })

Indian_News()
# News_object = News()