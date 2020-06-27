
import urllib, os, requests, datetime, subprocess
import feedparser

class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )
        print("Today's News: ")
        for i in range(0, 20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


News_object = News()
if __name__ == "__main__":
    News_object.Indian_News()
    
   