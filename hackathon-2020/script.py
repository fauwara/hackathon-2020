import urllib, os, requests, datetime, subprocess
import feedparser
from nsetools import Nse

data_news = []
data_tech = []

class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )

        for i in range(0, 10):
            entry = newsfeed.entries[i]
            
            data_news.append({
                "title" : entry.title,
                "summary" : entry.summary,
                "link" : entry.link 
                })


class Medium:
    
    def Tech_News(self):
        feed = feedparser.parse(
            "http://feeds.feedburner.com/gadgets360-latest?format=xml"
        )

        print("Tech News: ")
        for i in range(10):
            entry = feed.entries[i]

            data_tech.append({
                "title" : entry.title,
                "link" : entry.link 
                })
           

class StockExchange:
    def nse_stock(self):
        nse = Nse()
        print("TOP GAINERS OF YESTERDAY")
        print(nse.get_top_gainers())
        print('-------------------------------------------------------------------------------------------------------')
        print("TOP LOSERS OF YESTERDAY")
        print(nse.get_top_losers())
      
       

News_object = News()
Medium_object = Medium()
StockExchange_object = StockExchange()
if __name__ == "__main__":
   
    News_object.Indian_News()
    Medium_object.Tech_News()
    StockExchange_object.nse_stock()