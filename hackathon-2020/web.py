import urllib, os, requests, datetime, subprocess
import feedparser
from bs4 import BeautifulSoup
from requests import get

data_news = []
data_tech = []

def Indian_News():
    newsfeed = feedparser.parse(
        "http://feeds.feedburner.com/ndtvnews-india-news"
    )

    for i in range(10):
        entry = newsfeed.entries[i]
        
        # print(entry.title)
        # print(entry.summary)
        # print(entry.link)

        data_news.append({
            "title" : entry.title,
            "summary" : entry.summary,
            "link" : entry.link 
            })


def Tech_News():
        feed = feedparser.parse(
            "http://feeds.feedburner.com/gadgets360-latest?format=xml"
        )

        for i in range(10):
            entry = feed.entries[i]

            data_tech.append({
                "title" : entry.title,
                "link" : entry.link 
                })

Indian_News()
Tech_News()


# News_object = News()

# table table-condensed table-bordered table-hover table-striped
sahyadri_buzz_soup = BeautifulSoup(get("https://www.sahyadri.edu.in/NewsMedia/Daily").content, "html.parser")

table_soup = sahyadri_buzz_soup.find('table',class_ = "table table-condensed table-bordered table-hover table-striped")

table_body_soup = table_soup.tbody

info_td = table_body_soup.find_all('td')

topics = []

for i in range(2,len(info_td),3):
    # print(i)
    topics.append(info_td[i].a.text)

#print(type(info_td))